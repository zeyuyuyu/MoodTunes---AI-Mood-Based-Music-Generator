from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_moodtunes_basic_functionality():
    driver = webdriver.Chrome()
    try:
        # Load the app
        driver.get('http://localhost:8000')
        
        # Test UI elements presence
        assert 'MoodTunes' in driver.title
        assert driver.find_element(By.ID, 'mood-canvas')
        assert driver.find_element(By.ID, 'play-btn')
        
        # Test play button functionality
        play_btn = driver.find_element(By.ID, 'play-btn')
        play_btn.click()
        time.sleep(1)
        assert 'Pause' in play_btn.text
        
        # Test mood board interaction
        canvas = driver.find_element(By.ID, 'mood-canvas')
        actions = ActionChains(driver)
        actions.move_to_element(canvas)
        actions.move_by_offset(50, 50)
        actions.perform()
        time.sleep(2)
        
        # Test pause functionality
        play_btn.click()
        assert 'Play' in play_btn.text
        
    finally:
        driver.quit()

if __name__ == '__main__':
    test_moodtunes_basic_functionality()