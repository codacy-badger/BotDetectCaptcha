[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
[![HitCount](http://hits.dwyl.com/ikostan/BotDetectCaptcha.svg)](http://hits.dwyl.com/ikostan/BotDetectCaptcha)
![GitHub forks](https://img.shields.io/github/forks/ikostan/BotDetectCaptcha)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ikostan/BotDetectCaptcha)
![Maintenance](https://img.shields.io/maintenance/yes/2020)
![GitHub All Releases](https://img.shields.io/github/downloads/ikostan/BotDetectCaptcha/total)
![GitHub issues](https://img.shields.io/github/issues-raw/ikostan/BotDetectCaptcha)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/ikostan/BotDetectCaptcha)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
<a href="https://dependabot.com" rel="nofollow"><img src="https://camo.githubusercontent.com/35a144257b9aec7d472244f972d918c3926d5518/68747470733a2f2f6170692e646570656e6461626f742e636f6d2f6261646765732f7374617475733f686f73743d676974687562267265706f3d79737331342f6d757369637368617265" alt="Dependabot Status" data-canonical-src="https://api.dependabot.com/badges/status?host=github&repo=ikostan/BotDetectCaptcha" style="max-width:100%;"></a>
[![Netlify Status](https://api.netlify.com/api/v1/badges/ad3093c1-2604-4a11-9cdc-ca727460baa7/deploy-status)](https://app.netlify.com/sites/captcha-recognition-bot-allure-report/deploys)
[![Build Status](https://travis-ci.org/ikostan/BotDetectCaptcha.svg?branch=master)](https://travis-ci.org/ikostan/BotDetectCaptcha)
[![codecov](https://codecov.io/gh/ikostan/BotDetectCaptcha/branch/master/graph/badge.svg)](https://codecov.io/gh/ikostan/BotDetectCaptcha)

<br/>   
<div align="center"> 
<img width="10%" height="10%" src="https://github.com/ikostan/BotDetectCaptcha/blob/master/img/python_logo.PNG" hspace="20">
<img width="12%" height="12%" src="https://github.com/ikostan/BotDetectCaptcha/blob/master/img/selenium-computer-icon.jpg" hspace="10">
<img width="18%" height="18%" src="https://github.com/ikostan/BotDetectCaptcha/blob/master/img/artificial-intelligence.png" hspace="10">
</div>
<br/>

# Captcha Recognition Bot

"Captcha Recognition Bot" framework with Python, Selenium, and Machine Learning.

### Table of Contents

1. <a href="#about">About the project</a>
2. <a href="#doc">Official Documentation</a>
3. <a href="#compression">Image Compression</a>
4. <a href="#dev">Dev Environment</a>
5. <a href="#tech_issues">Tech Issues and Problem Solving</a>
6. [Selenium Webdriver](https://github.com/ikostan/BotDetectCaptcha/tree/master/drivers):<br/>
    - [ChromeDriver](https://github.com/ikostan/BotDetectCaptcha/tree/master/drivers/chrome)<br/>
    - [Microsoft WebDriver](https://github.com/ikostan/BotDetectCaptcha/tree/master/drivers/microsoft_edge)<br/>
    - [geckodriver](https://github.com/ikostan/BotDetectCaptcha/tree/master/drivers/mozilla_geckodriver)<br/>
7. [Web Element](https://github.com/ikostan/BotDetectCaptcha/tree/master/element_object_models)<br/>
8. [Expected Results](https://github.com/ikostan/BotDetectCaptcha/tree/master/expected_results)<br/>
9. [Page/Element Locators](https://github.com/ikostan/BotDetectCaptcha/tree/master/page_locators)<br/>
    - [UML diagram](https://github.com/ikostan/BotDetectCaptcha/tree/master/page_locators/uml)
10. [Page Object Model (POM)](https://github.com/ikostan/BotDetectCaptcha/tree/master/page_object_models)<br/>
11. [Tests](https://github.com/ikostan/BotDetectCaptcha/tree/master/tests)<br/>
    i. [Content Tests](https://github.com/ikostan/BotDetectCaptcha/tree/master/tests/content_tests)<br/>
        - [Base Cases](https://github.com/ikostan/BotDetectCaptcha/tree/master/tests/content_tests/base_cases)<br/>
        - [Base Content Tests](https://github.com/ikostan/BotDetectCaptcha/tree/master/tests/content_tests/base_content_tests)<br/>
        - [Unique Content Tests](https://github.com/ikostan/BotDetectCaptcha/tree/master/tests/content_tests/base_content_tests)
12. [Software](https://github.com/ikostan/BotDetectCaptcha/tree/master/software)<br/>
13. [CAPTCHA Images](https://github.com/ikostan/BotDetectCaptcha/tree/master/captcha_images)<br/>
    1. [BotDetect CAPTCHA Images](https://github.com/ikostan/BotDetectCaptcha/tree/master/captcha_images/bot_detect)<br/>
        - [AncientMosaic CAPTCHA Images](https://github.com/ikostan/BotDetectCaptcha/tree/master/captcha_images/bot_detect/ancient_mosaic)<br/>
14. <a href="#browsers">Supported Web Browsers</a>
15. <a href="#disclaimer">Disclaimer</a>

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

### Image Compression
<a id="compression"></a>

Images are one of the key parts of the application, but they also play a really big role in performance degradation. The more images you have, the slower your load times can become.

[IMGBOT](https://imgbot.net/docs/#docs) running a loss-less compression that and takes the heavy lifting out for you. With just a couple of clicks you can get `IMGBOT` running in your project's repo on GitHub and sending you pull requests with your images optimized.

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

### Allure test report

Lates Allure test report you can check [here](https://captcha-recognition-bot-allure-report.netlify.com).

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

<details>
  <summary><b>How to generate Allure report with history trends (Windows OS)</b></summary>

<br/>Step by step:

1. Run tests from pytest using following arguments: -v --alluredir=allure-results

2. Copy '.\allure-report\history\' folder into '.\allure-results\history\'

3. Run: allure generate .\allure-results\ -o .\allure-report\ --clean

4. Following output should appear: Report successfully generated to .\allure-report

5. Run: allure open .\allure-report\

[Source](https://github.com/allure-framework/allure2/issues/813)
</details>

<details>
  <summary><b>Sphinx Documentation Set Up</b></summary>

<br/>Step by step:

1. Create docs directory

2. Open cmd > Go to docs directory

3. cmd > Run: sphinx-quickstart. **Note:** run with default answers
    
4. Go to docs/conf.py

5. Uncomment following lines:

```python
    import os
    import sys
    sys.path.insert(0, os.path.abspath('.'))
```

6. Update extensions list as following:

```python
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
```

7. Update template as following:

```python
html_theme = 'sphinx_rtd_theme'

```

8. Update sys.path.insert as following:

```python
sys.path.insert(0, os.path.abspath('..'))
```

9. Go to docs/index.rst > add modules, see example below:

```bash

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
```

10. Open cmd > run: 

```python
sphinx-apidoc -o . ..
```

11. cmd > Run: make html

12. Install html template:

```python
pip install sphinx_rtd_theme
```

[Video Tutorial](https://www.youtube.com/watch?v=b4iFyrLQQh4)
[Sphinx Documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
[More Info](https://stackoverflow.com/questions/13516404/sphinx-error-unknown-directive-type-automodule-or-autoclass)
</details>

<details>
  <summary><b>Auto-Generated Python Documentation with Sphinx</b></summary>

<br/>Step by step:

1. Open CMD

2. Go to docs directory

3. Run: make clean

4. Run: sphinx-apidoc -o . ..

5. Add doc files name into relevant doc rst file

6. Run: make html

[Source](https://www.youtube.com/watch?v=b4iFyrLQQh4)
</details>

<details>
  <summary><b>Read-the-docs build fails with “cannot import name 'PackageFinder' from 'pip._internal.index'</b></summary>
    <p></p>
The issue and the fix are described in read-the-docs issue [#6554](https://github.com/readthedocs/readthedocs.org/issues/6554):

The fix is to wipe out the build environment as follows (this is taken from [here](https://docs.readthedocs.io/en/stable/guides/wipe-environment.html)):

* Log in to read-the-docs
* Go to Versions
* Click on the Edit button of the version you want to wipe on the right side of the page
* Go to the bottom of the page and click the wipe link, next to the “Save” button
* Now you can re-build the version with a fresh build environment!

This fix worked for me (but as of 26-Jan-2020 you have to wipe out the environment for every build -- see comment from Grimmy below).

[Source](https://stackoverflow.com/questions/59846065/read-the-docs-build-fails-with-cannot-import-name-packagefinder-from-pip-in)
</details>

<details>
  <summary><b>Using Codecov With Travis-CI (pytest-cov)</b></summary>
    
<br/>   
<div align="center"> 
<img src="https://github.com/ikostan/BotDetectCaptcha/blob/master/img/codecov.png" hspace="20">
</div>
<br/>

Continuous Integration has brought about so much ease in ensuring quality code is pushed. Making developer lives easier, but it doesn't end there, testing is just a part of bigger picture. We also need to capture the test coverage, we want to assess the quality of our code by ensuring our tests meet the minimum threshold. For this we turn to pytest-cov.
Since we have Travis-CI already set up for our python project, let's add CodeCov to ensure we generate coverage reports from `.travis.yml`. To connect Github to Codecov is as easy as signing up with our Github account.

We can now proceed to our local machine and install pytest-cov, just by running `pip install pytest-cov pytest` then add codecov tool `pip install codecov`.
Generate a new requirements file, simply `run pip freeze > requirements.txt`

Afterwards, we open your `.travis.yml` file and add:

```text
   install:
    - pip install -r requirements.txt

   script:
    - py.test  --cov-report term --cov=app/test/

   env:
    - CODECOV_TOKEN=<token>#IF ONLY YOU HAVE A PRIVATE REPOSITORY

   after_success:
    - codecov
```

[Source](https://dev.to/j0nimost/using-codecov-with-travis-ci-pytest-cov-1dfj)
</details>
