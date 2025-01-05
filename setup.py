from setuptools import setup, find_packages

setup(
    name='jjd-chat-ai',
    version='0.1.0',
    description='Question and Answer Chat for the Blog content - powered by AI',
    author='Jacek Jabłonka',
    author_email='kontakt@juniorjavadeveloper.pl',
    url='https://www.juniorjavadeveloper.pl/en/',
    packages=find_packages(include=['app', 'app.*', 'web', 'web.*']),
    install_requires=[
        'streamlit',
        'python-dotenv',
        'langchain-community',
    ],
    entry_points={
        'console_scripts': [
            'jjd-chat-ai=web.jjd_chat_ai_web.com.machinelearning.apps.useful.jjdchatai.web.web_app:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)