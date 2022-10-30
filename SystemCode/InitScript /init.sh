echo  "\033[36mWelcome to use this system, it may take a few minutes to set up the environment\033[0m"
echo  "\033[35mBefore initiation please make sure you have download the MySQL\033[0m"
echo  "\033[35mand switched to your Python virtual environment\033[0m"
echo  " "
echo  "\033[32m***********Init Database by using default config.....************\033[0m"
echo  "to change the password used, please refer to this script and modify the line"
echo  "- python init_database.py [new password]"
cd InitScript 
python init_database.py 12345678
echo  " "
echo "\033[34m==================================================================\033[0m"
echo  " "
echo  "\033[32m***************Download Python packages...***********************\033[0m"
echo  " "
echo "Python detected Version:"
python --version
cd ..
cd project/Group11_project1
pip install -r requirements.txt
echo  "\033[32m***************Python packages all downloaded*********************\033[0m"
echo  " "
echo "\033[34m================Environment set up successfully====================\033[0m"

