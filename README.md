This is a Generative AI sample project which uses openai llm to generate mcq based on data given by user. User can input data, 
difficulty level, number of mcq and topic. This has two LLM's connected using langchain. First LLMChain generate MCQ, second
one check and updates it. It also provide a review of MCQ's.

This is a simple project which you can use for learning purposes. The following steps for creating this project will help you to get
an overall idea of project setup. Reading this along with source code will help you to get overall picture of how to setup a project
and run it in aws cloud.

Clone this on any cloud server like Amazon AWS EC2 instance and make it live.

1. Install vscode, python plugins
2. Install git
3. open cmd, goto workfolder, execute -> code .    (This will open vscode in that directory)
4. Open a 'Git Bash' terminal (Terminal -> New Terminal and then select git bash)
5. Execute git init command in terminal to create a local repository
6. Create a file README.md  (mark down file)
7. commit and publish readme.md to git server (If error set user and email using "git --global user=")
8. view->command pallette->select python interpreter-> select base env interpretor
9. in terminal execute "conda create -p env python=3.8 -y" to create new environment env
10. execute "source activate ./env " to make it default env for this project
11. create a file .gitignore using ide or touch command. add text 'env' to .gitignore to remove env from publishing to git
12. create file requirement.txt with openai,langchain,streamlit,python-dotenv,PyPDF2,langchain_community
13. create a file setup.py and add code
	
from setuptools import setup, find_packages
setup(
    name='mcqgenerator',
    version='0.0.1',
    author='adeeb',
    author_email='adeeb.arangodan@gmail.com',
    install_requires=['openai', 'langchain', 'streamlit', 'python-dotenv', 'PyPDF2'],
    packages=find_packages()
)

14. open requirement.txt and add new line '-e .' to execute setup.py after the installation of packages in requiremnet.txt
15. create a folder src. add a file __init__.py to make it a package
16. inside src create a folder mcqgenerator and add a file __init__.py to make it a package
17. add a folder experiment and add a file mcq.ipynb
18. pip install -r requirement.txt
19. you will get a folder mcqgenerator.egg-info containing metadata of new package installed.
20. open mcq.ipynb and set kernel to python in 'env' environment
21. create a file .env to store environment variable and add .env to .gitignore
22. from dotenv import load_dotenv
    load_dotenv()
    os.getenv('OPENAI_API_KEY') will load OPENAI_API_KEY in .env file
23. add .env to .gitignore
24. Create a StreamlitApp.py file with create a ui
25. mcqgenerator.py file has code to create LLM, LLMChain, SequentialChain etc
26. run the app using command: streamlit run StreamlitApp.py.

27. On aws cloud server using linux, use this code to clone the repo and make the project live
    sudo apt update
    sudo apt-get update
    sudo apt upgrade -y
    sudo apt install git curl unzip tar make sudo vim wget -y

    git clone "Your-repository"
    sudo apt install python3-pip, python3-venv
    python3 -m venv <your envname>
    cd <envname>/bin/activate
    pip3 install -r requirements.txt
    python3 -m streamlit run StreamlitAPP.py

28. if you want to add openai api key
    create .env file in your server touch .env
    vi .env #press insert #copy your api key and paste it there #press and then :wq and hit enter

29. go with security and add the inbound rule add the port 8501