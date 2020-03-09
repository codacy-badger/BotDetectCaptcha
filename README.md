[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

<br/>   
<div align="center"> 
<img width="10%" height="10%" src="https://github.com/ikostan/BotDetectCaptcha/blob/master/img/python_logo.PNG" hspace="20">
<img width="12%" height="12%" src="https://github.com/ikostan/BotDetectCaptcha/blob/master/img/selenium-computer-icon.jpg" hspace="10">
<img width="18%" height="18%" src="https://github.com/ikostan/BotDetectCaptcha/blob/master/img/artificial-intelligence.png" hspace="10">
</div>
<br/>

# BotDetect Captcha Recognition

Captcha recognition framework with Python, Selenium, and Machine Learning.

### Table of Contents

1. <a href="#about">About the project</a>
2. <a href="#doc">Official Documentation</a>
3. <a href="#dev">Dev Environment</a>
4. <a href="#tech_issues">Tech Issues and Problem Solving</a>
5. [Selenium Webdriver](https://github.com/ikostan/BotDetectCaptcha/tree/master/drivers):<br/>
    - [ChromeDriver](https://github.com/ikostan/BotDetectCaptcha/tree/master/drivers/chrome)<br/>
    - [Microsoft WebDriver](https://github.com/ikostan/BotDetectCaptcha/tree/master/drivers/microsoft_edge)<br/>
    - [geckodriver](https://github.com/ikostan/BotDetectCaptcha/tree/master/drivers/mozilla_geckodriver)<br/>
6. [Web Element](https://github.com/ikostan/BotDetectCaptcha/tree/master/element_object_models)<br/>
7. [Expected Results](https://github.com/ikostan/BotDetectCaptcha/tree/master/expected_results)<br/>
8. [Page/Element Locators](https://github.com/ikostan/BotDetectCaptcha/tree/master/page_locators)<br/>
    - [UML diagram](https://github.com/ikostan/BotDetectCaptcha/tree/master/page_locators/uml)
9. [Page Object Model (POM)](https://github.com/ikostan/BotDetectCaptcha/tree/master/page_object_models)<br/>
10. [Tests](https://github.com/ikostan/BotDetectCaptcha/tree/master/tests)<br/>
    i. [Content Tests](https://github.com/ikostan/BotDetectCaptcha/tree/master/tests/content_tests)<br/>
        - [Base Cases](https://github.com/ikostan/BotDetectCaptcha/tree/master/tests/content_tests/base_cases)<br/>
        - [Base Content Tests](https://github.com/ikostan/BotDetectCaptcha/tree/master/tests/content_tests/base_content_tests)<br/>
        - [Unique Content Tests](https://github.com/ikostan/BotDetectCaptcha/tree/master/tests/content_tests/base_content_tests)
11. [Software](https://github.com/ikostan/BotDetectCaptcha/tree/master/software)<br/>
12. [CAPTCHA Images](https://github.com/ikostan/BotDetectCaptcha/tree/master/captcha_images)<br/>
    1. [BotDetect CAPTCHA Images](https://github.com/ikostan/BotDetectCaptcha/tree/master/captcha_images/bot_detect)<br/>
        - [AncientMosaic CAPTCHA Images](https://github.com/ikostan/BotDetectCaptcha/tree/master/captcha_images/bot_detect/ancient_mosaic)<br/>
13. <a href="#browsers">Supported Web Browsers</a>
14. <a href="#disclaimer">Disclaimer</a>

### About the project

<a id="about"></a>

The main purpose is to learn machine learning platform and demonstrate the professional abilities of writing Captcha recognition framework using the Python language,Selenium and Machine Learning. 

[BotDetect CAPTCHA project](https://captcha.com) is used as a source for captcha images. [This page](https://captcha.com/demos/features/captcha-demo.aspx) demonstrates how powerful and customizable BotDetect is. Feel free to experiment with various BotDetect Captcha parameters and their combinations.

As a reference for the project I used [TensorFlow CAPTCHA solver](https://pylessons.com/TensorFlow-CAPTCHA-solver-training/) tutorials.

**Main Objectives:**<br/>

- Create Captcha recognition automation using Machine Learning and Selenium Automation framework<br/>
- Build fast and readable automation using minimal code<br/>
- Showcase with effective way to identify web elements<br/>
- [Page Objects](https://github.com/SeleniumHQ/selenium/wiki/PageObjects) and [Element Objects](https://www.tutorialspoint.com/dom/dom_element_object) implementation (see [Page Object Model (POM)](https://github.com/ikostan/BotDetectCaptcha/tree/master/page_object_models) and [Element Object](https://github.com/ikostan/BotDetectCaptcha/tree/master/elements))<br/>
- Arrange, Act and Assert (AAA) Pattern implementation (see [step_definition](https://github.com/ikostan/ParaBankSeleniumAutomation/tree/master/utils))<br/>
- Industry-ready test structure<br/>
- Cross-browsing testing (see [Config](https://github.com/ikostan/BotDetectCaptcha/blob/master/tests/config.py) class and [get_args_from_cli](https://github.com/ikostan/BotDetectCaptcha/blob/master/utils/get_args_from_cli.py) file)<br/>
- Ability to pass arguments from CLI (see [get_args_from_cli](https://github.com/ikostan/BotDetectCaptcha/blob/master/utils/get_args_from_cli.py) file)
- Build readable test report using Allure Framework<br/>
- Test code should avoid violating principles like [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it), [SRP](https://en.wikipedia.org/wiki/Single_responsibility_principle) and [KISS](https://en.wikipedia.org/wiki/KISS_principle).
- Integration with [Travis CI](https://travis-ci.org/)
- Using real-like web app ([BotDetect CAPTCHA Demo](https://captcha.com/demos/features/captcha-demo.aspx)) in order to accomplish all the above<br/>

### Official Documentation:<br/>
<a id="doc"></a>

**Additional Resources:**<br/>

- [Selenium Documentation](https://seleniumhq.github.io/selenium/docs/api/py/api.html)<br/>
- [Full Pytest documentation](http://doc.pytest.org/en/latest/contents.html)<br/>
- ['Selenium with Python' official documentation webpage](https://selenium-python.readthedocs.io)<br/>
- [PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html)<br/>
- [Allure Framework](https://docs.qameta.io/allure/)<br/>
- [TensorFlow CAPTCHA solver](https://pylessons.com/TensorFlow-CAPTCHA-solver-training/)<br/>
- [BotDetect CAPTCHA Generator](https://captcha.com/)<br/>

### Dev Environment

<a id="dev"></a>

1. [Python 3.7.4](https://www.python.org/downloads/release/python-374/)<br/>
2. [Selenium 3.141.0](https://pypi.org/project/selenium/)<br/>
3. [PyTest 5.3.5](https://pypi.org/project/pytest/)<br/>
4. [Allure Framework 2.12.1](http://allure.qatools.ru/)<br/>
5. [Win 10 (64 bit)](https://www.microsoft.com/en-ca/software-download/windows10)<br/>
6. [PyCharm 2019.3 (Community Edition)](https://www.jetbrains.com/pycharm/download/#section=windows)<br/>
7. [GitHub Desktop 2.3.1](https://desktop.github.com/)<br/>
8. [GIT 2.22.0.windows.1](https://git-scm.com/download/win)<br/>
9. [Java SE 8](https://www.oracle.com/technetwork/java/javase/overview/index.html)<br/>
10. [LabelImg GitHub link](https://github.com/tzutalin/labelImg)<br/>
11. [LabelImg download link](https://www.dropbox.com/s/tq7zfrcwl44vxan/windows_v1.6.0.zip?dl=1)<br/>

### Python Packages

Full list of dependencies see [here.](https://github.com/ikostan/BotDetectCaptcha/blob/master/requirements.txt)

### Nice to have tools

1. [Fiddler: The free web debugging proxy](https://www.telerik.com/fiddler)
2. [Kite: Code Faster in Python](https://kite.com/)
3. [Ragnorex: Smart Selector Generator](https://www.ranorex.com/selocity/browser-extension)
4. [Pynsource: Python source code into UML diagrams](https://www.pynsource.com/index.html)

**Note:** In order to instantiate webdriver I use Driver class of my own. For more info please look [here](https://github.com/ikostan/BotDetectCaptcha/tree/master/utils).<br/>

### Supported/tested browsers

<a id="browsers"></a>

- Chrome: v80 (64 bit)
- Firefox: v73 (64  bit)
- Edge: v18.18362

### Disclaimer

<a id="disclaimer"></a>

Using this software to violate the terms and conditions of any third-party service is strictly against the intent of this software. By using this software, you are acknowledging this fact and absolving the author or any potential liability or wrongdoing it may cause. This software is meant for testing and experimental purposes only, so please act responsibly.

### Tech Issues and Problem Solving

<a id="tech_issues"></a>

<details>
  <summary><b>Changing the project interpreter in the PyCharm project settings</b></summary>

<br/>1. In the **Settings/Preferences dialog** (Ctrl+Alt+S), select **Project <project name> | Project Interpreter**.<br/>
2. Expand the list of the available interpreters and click the **Show All** link.<br/>
3. Select the target interpreter. When PyCharm stops supporting any of the outdated Python versions, the corresponding project interpreter is marked as unsupported.<br/>
4. The Python interpreter name specified in the **Name** field, becomes visible in the list of available interpreters. Click **OK** to apply the changes.<br/>

For more info please check [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)<br/>

</details>


<details>
  <summary><b>PyCharm - Choosing Your Testing Framework</b></summary>
 
<br/>1. Open the Settings/Preferences dialog, and under the node Tools, click the page **Python Integrated Tools**.<br/>
2. On this page, click the **Default Test Runner** field.<br/>
3. Choose the desired test runner:<br/>

<br/>   
<div align="center"> 
<img width="60%" height="60%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/py_choosing_test_runner.png" hspace="20">
</div>
<br/>

For more info please see [Enable Pytest for you project](https://www.jetbrains.com/help/pycharm/pytest.html)
</details>


<details>
  <summary><b>Setting up Python3 virtual environment on Windows machine</b></summary>
<br/>

1. open CMD<br/>
2. navigate to project directory, for example:<br/> 

```bash
cd C:\Users\superadmin\Documents\GitHub\CaptchaRecognition\BotDetectCaptcha
```

3. run following command:<br/> 

```bash 
pip install virtualenv
```

4. run following command:<br/> 

```bash 
virtualenv venv --python=python
```
    
</details>


<details>
  
  <summary><b>Activate Virtual Environment</b></summary>

  <br/>
  In a newly created virtualenv there will be a bin/activate shell script. For Windows systems, activation scripts are provided for CMD.exe and Powershell.
  <br/><br/>

  1. Open Terminal<br/>
  2. Run: \path\to\env\Scripts\activate 
  
  <br/>Source: https://pypi.org/project/virtualenv/1.8.2/
  
</details>


<details>
  <summary><b>Auto generate requirements.txt</b></summary>

<br/>Any application typically has a set of dependencies that are required for that application to work. The requirements file is a way to specify and install specific set of package dependencies at once.<br/>
Use pip’s freeze command to generate a requirements.txt file for your project:<br/>

```python
    pip freeze > requirements.txt
```

If you save this in requirements.txt, you can follow this guide: [PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html), or you can:<br/>
   
```python
    pip install -r requirements.txt
```   
Source: https://www.idiotinside.com/2015/05/10/python-auto-generate-requirements-txt/<br/>
</details>


<details>
  <summary><b>How to fix in case .gitignore is ignored by Git</b></summary>

<br/>Even if you haven't tracked the files so far, Git seems to be able to "know" about them even after you add them to .gitignore.<br/> 

**NOTE:**<br/>
    - First commit your current changes, or you will lose them.<br/> 
    - Then run the following commands from the top folder of your Git repository:<br/> 
    
```bash 
    git rm -r --cached .
    git add .
    git commit -m "fixed untracked files"
```
    
</details>


<details>
  <summary><b>Common Selenium errors</b></summary>

<br/>- **[How to fix common Selenium errors?](https://www.ultimateqa.com/common-selenium-webdriver-errors-fix/)**<br/>

</details>


<details>
  <summary><b>Microsoft webdriver for edge 18 and above</b></summary>

<br/>MS made WebDriver a Windows Feature on Demand (FoD), which ensures that it’s always up to date automatically, and enables some new ways to get Microsoft WebDriver.<br/>
    
The simplest way to get started is simply to enable Developer Mode. Simply open the Settings app and go to “Update & Security,” “For developers,” and select “Developer Mode.” The appropriate version of WebDriver will be automatically installed.<br/>
    
You can also install a standalone version of WebDriver in one of two ways:<br/>
    * Search “Manage optional features” from Start, then select “Add a Feature,” “WebDriver.”<br/>
    * Install via DISM by running the following command in an elevated command prompt:
    <br/>```DISM.exe /Online /Add-Capability /CapabilityName:Microsoft.WebDriver~~~~0.0.1.0```<br/>

<br/>   
<div align="center"> 
<img width="60%" height="60%" src="https://github.com/ikostan/BotDetectCaptcha/blob/master/img/MS_Edge_driver_install.PNG" hspace="20">
</div>
<br/>

This also means that MS will no longer be providing standalone downloads for Microsoft WebDriver going forward<br/>
Source: https://blogs.windows.com/msedgedev/2018/06/14/webdriver-w3c-recommendation-feature-on-demand/#Rg8g2hRfjBQQVRXy.97

</details>


<details>
  <summary><b>Test are failed due to slow performance of WebDriver</b></summary>
  
<br/>Explicit wait is used to specify wait condition for a particular element.<br/> 
Here we define to wait for a certain condition to occur before proceeding further in the code.

```python
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    
    # Wait for element to appear:
    wait = WebDriverWait(self.driver, 10)
    wait.until(ec.title_is(self.new_window_name))
```

</details>


<details>
  <summary><b>How to Get Selenium to Wait for Page Load After a Click</b></summary>
  
<br/>It turns out Selenium has a built-in condition called staleness_of, as well as its own wait-for implementation. 
Use them, alongside the @contextmanager decorator and the magical-but-slightly-scary yield keyword, and you get:

```python
    from contextlib import contextmanager
    from selenium.webdriver.support.ui import WebDriverWait 
    from selenium.webdriver.support.expected_conditions import staleness_of
    
    class MySeleniumTest(SomeFunctionalTestClass): 
      # assumes self.browser is a selenium webdriver
    
      @contextmanager
      def wait_for_page_load(self, timeout=30):
        old_page = self.browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.browser, timeout).until(
          staleness_of(old_page)
        )
        
      def test_stuff(self):
        # example use
        with self.wait_for_page_load(timeout=10):
          self.browser.find_element_by_link_text('a link')
```
    
**Note** that this solution only works for “non-JavaScript” clicks, i.e., clicks that will cause the browser to load a brand new page, and thus load a brand new HTML body element.
<br/>Source: https://blog.codeship.com/get-selenium-to-wait-for-page-load/

</details>


<details>
  
  <summary><b>error: RPC failed; curl 56 Recv failure: Connection was reset</b></summary>
  <br/>
  1. Open Git Bash<br/>
  2. Run: "git config --global http.postBuffer 157286400" 
  
  <br/>Source: https://stackoverflow.com/questions/36940425/gitlab-push-failed-error
  
</details>

<details>
  
  <summary><b>py.test: error: unrecognized arguments</b></summary>

  Note that pytest does not find conftest.py files in deeper nested sub directories at tool startup. 
  It is usually a good idea to keep your conftest.py file in the top level test or project root directory.

  One solution is to create an external plugin, or move the option to a conftest file nearer the root.

  <br/>Source: https://stackoverflow.com/questions/31522783/py-test-error-unrecognized-arguments/31526934

</details>