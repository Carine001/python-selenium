import requests
import io
import random
import time
import sys

# Speech Recognition Imports
from pydub import AudioSegment
import speech_recognition as sr

# Selenium
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver

# check if using python 3
if sys.version_info[0] >= 3:
    xrange = range

chrome_service = ChromeService(r"C:\Users\wassi\source\repos\python-selenium\drivers\chrome-driver.exe")

# Randomization Related
MIN_RAND = 0.64
MAX_RAND = 1.27
LONG_MIN_RAND = 4.78
LONG_MAX_RAND = 11.1

NUMBER_OF_ITERATIONS = 100
RECAPTCHA_PAGE_URL = "https://www.google.com/recaptcha/api2/demo"

HOUNDIFY_CLIENT_ID = "-Ggp-OsEavO4-XnxqZC2vg=="
HOUNDIFY_CLIENT_KEY = "MGSBbNpn2r2BObVV829gBpk7xP2Ie3eUWfwuSdUaP2-YWrZLvE8cjij8GYq6u3G0VJob1UNFI0JsNdeygGmBdg=="

DIGITS_DICT = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


class breakCaptcha(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_service)

    def is_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    def get_recaptcha_challenge(self):
        while 1:
            # Navigate to a ReCaptcha page
            self.driver.get(RECAPTCHA_PAGE_URL)
            time.sleep(random.uniform(MIN_RAND, MAX_RAND))

            # Get all the iframes on the page
            iframes = self.driver.find_elements(By.TAG_NAME, "iframe")

            # Switch focus to ReCaptcha iframe
            self.driver.switch_to.frame(iframes[0])
            time.sleep(random.uniform(MIN_RAND, MAX_RAND))

            # Verify ReCaptcha checkbox is present
            if not self.is_exists_by_xpath('//div[@class="recaptcha-checkbox-checkmark" and @role="presentation"]'):
                print("[{0}] No element in the frame!!")
                continue

            # Click on ReCaptcha checkbox
            self.driver.find_element(
                By.XPATH, '//span[.//div[@class="recaptcha-checkbox-checkmark" and @role="presentation"]]'
            ).click()
            time.sleep(random.uniform(LONG_MIN_RAND, LONG_MAX_RAND))

            # Check if the ReCaptcha has no challenge
            if self.is_exists_by_xpath('//span[@aria-checked="true"]'):
                print("[{0}] ReCaptcha has no challenge. Trying again!")
            else:
                return

    def get_audio_challenge(self, iframes):
        # Switch to the last iframe (the new one)
        self.driver.switch_to.frame(iframes[-1])

        # Check if the audio challenge button is present
        if not self.is_exists_by_xpath('//button[@id="recaptcha-audio-button"]'):
            print("[{0}] No element of audio challenge!!")
            return False

        print("[{0}] Clicking on audio challenge")
        # Click on the audio challenge button
        self.driver.find_element(By.XPATH, '//button[@id="recaptcha-audio-button"]').click()
        time.sleep(random.uniform(LONG_MIN_RAND, LONG_MAX_RAND))

    def get_challenge_audio(self, url):
        # Download the challenge audio and store in memory
        request = requests.get(url)
        audio_file = io.BytesIO(request.content)

        # Convert the audio to a compatible format in memory
        converted_audio = io.BytesIO()
        sound = AudioSegment.from_mp3(audio_file)
        sound.export(converted_audio, format="wav")
        converted_audio.seek(0)

        return converted_audio

    def string_to_digits(self, recognized_string):
        return "".join([DIGITS_DICT.get(word, "") for word in recognized_string.split(" ")])

    def speech_to_text(self, audio_source):
        # Initialize a new recognizer with the audio in memory as source
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_source) as source:
            audio = recognizer.record(source)  # read the entire audio file

        audio_output = ""
        # recognize speech using Google Speech Recognition
        try:
            audio_output = recognizer.recognize_google(audio)
            print("[{0}] Google Speech Recognition: " + audio_output)
            # Check if we got harder audio captcha
            if any(character.isalpha() for character in audio_output):
                # Use Houndify to detect the harder audio captcha
                print("[{0}] Fallback to Houndify!")
                audio_output = self.string_to_digits(
                    recognizer.recognize_houndify(
                        audio,
                        client_id=HOUNDIFY_CLIENT_ID,
                        client_key=HOUNDIFY_CLIENT_KEY,
                    )
                )
                print("[{0}] Houndify: " + audio_output)
        except sr.UnknownValueError:
            print("[{0}] Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("[{0}] Could not request results from Google Speech Recognition service; {1}".format(e))

        return audio_output

    def solve_audio_challenge(self):
        # Verify audio challenge download button is present
        if not self.is_exists_by_xpath('//a[@class="rc-audiochallenge-download-link"]') and not self.is_exists_by_xpath(
            '//div[@class="rc-text-challenge"]'
        ):
            print("[{0}] No element in audio challenge download link!!")
            return False

        # If text challenge - reload the challenge
        while self.is_exists_by_xpath('//div[@class="rc-text-challenge"]'):
            print("[{0}] Got a text challenge! Reloading!")
            self.driver.find_element(By.ID, "recaptcha-reload-button").click()
            time.sleep(random.uniform(MIN_RAND, MAX_RAND))

        # Get the audio challenge URI from the download link
        download_object = self.driver.find_element(By.XPATH, '//a[@class="rc-audiochallenge-download-link"]')
        download_link = download_object.get_attribute("href")

        # Get the challenge audio to send to Google
        converted_audio = self.get_challenge_audio(download_link)

        # Send the audio to Google Speech Recognition API and get the output
        audio_output = self.speech_to_text(converted_audio)

        # Enter the audio challenge solution
        self.driver.find_element(By.ID, "audio-response").send_keys(audio_output)
        time.sleep(random.uniform(LONG_MIN_RAND, LONG_MAX_RAND))

        # Click on verify
        self.driver.find_element(By.ID, "recaptcha-verify-button").click()
        time.sleep(random.uniform(LONG_MIN_RAND, LONG_MAX_RAND))

        return True

    def solve(self):
        # Get a ReCaptcha Challenge
        self.get_recaptcha_challenge()

        # Switch to page's main frame
        self.driver.switch_to.default_content()

        # Get all the iframes on the page again- there is a new one with a challenge
        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")

        # Get audio challenge
        self.get_audio_challenge(iframes)

        # Solve the audio challenge
        if not self.solve_audio_challenge():
            return False

        # Switch to the ReCaptcha iframe to verify it is solved
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame(iframes[0])

        return self.is_exists_by_xpath('//span[@aria-checked="true"]')


def main():
    captchaBreaker = breakCaptcha()
    captchaBreaker.solve()


if __name__ == "__main__":
    main()
