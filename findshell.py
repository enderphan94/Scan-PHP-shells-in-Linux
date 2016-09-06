import re
from sys import argv
from os.path import exists
import optparse
import argparse
import glob
import os
import datetime
import stat
import pwd
import time

##################################################################################################################
#					SCAN SHELL TOOL	 							 #	
#			       	CODED by Big-Small Creep						         #
#               CODING WILL ChANGE THE WORLD - OTHERWISE IT COULD CHANGE YOUR MIND             			 #
#										                                 #
##################################################################################################################

parser = argparse.ArgumentParser()

parser.add_argument('-D','--dir',help='Input Directory You Want To Scan',required=True)
parser.add_argument('-d','--day',type=int,help='You can choose what date you want to scan util today',required=False)
parser.add_argument('-t','--type',help="Chose file types you want to scan or blank if you want to scan fully (e.g: .php, .html) ",required=False)

args =parser.parse_args()

dir = args.dir
day = args.day
type= args.type

if not os.path.exists(dir):
        print " Directory entered does not exist?"
else:
	
	def input_day(file_name):
		
		if day is not None:
			
			hour = day * 24
			today =  datetime.datetime.now()	
			#someday = today - datetime.timedelta(hours=hour)
			file_date = datetime.datetime.utcfromtimestamp(os.path.getmtime(file_name))
			
			sub_time = today - file_date
			
			if (sub_time < datetime.timedelta(hours=hour)):
				return oct(os.stat(file_name)[0])[-3:],pwd.getpwuid(os.stat(file_name).st_uid)[0],modi_date(file_name),file_name
				
			else:
				return "";
		else:
			return oct(os.stat(file_name)[0])[-3:],pwd.getpwuid(os.stat(file_name).st_uid)[0],modi_date(file_name),file_name
		#return someday.strftime("%Y-%m-%d")		

	def modi_date(file_name): # file time

		return time.strftime("%Y-%m-%d", time.gmtime(os.path.getmtime(file_name)))

	
	def own(file_name):       #file permission
		 
		return getpwuid(stat(file_name).st_uid).pw_name


	def open_file(dir_file): #Open file
		
       		cross_file = open(dir_file,'r')
        	o_cross_file = cross_file.read()
        	cross_file.close()
        	matches = filenames.findall(o_cross_file)
		if len(matches) != 0:
			#print oct(os.stat(dir_file)[0])[-3:],pwd.getpwuid(os.stat(dir_file).st_uid)[0],input_day(dir_file),matches
			print input_day(dir_file)
			#randay =  modi_date(dir_file) + datetime.date.today()
			#print randay.days
			#print datetime.date.today()
	def open_folder(dir_folder): #Open Folder

		if type is not None:
			for file1 in glob.glob(dir_folder+"/*"+type):
				if os.path.isfile(file1):
                        		open_file(file1)		                
				if os.path.isdir(file1):		
                       			open_folder(file1)
		else:
			for file1 in glob.glob(dir_folder+"/*"):
                                if os.path.isfile(file1):
                                        open_file(file1)
                                if os.path.isdir(file1):
                                        open_folder(file1)
	# Main()	
	patternarray = ['cmd', 'ender' ,'hello']
	print "\nthe files listed below are might be the shell \n"

        for x in patternarray:

		filenames = re.compile(r""+x)
		if type is not None:
                
                	for file in glob.glob(dir+"/*"+type):

                       		if os.path.isfile(file):
                               		open_file(file)
                       		if os.path.isdir(file):
                               		open_folder(file)
		else:
			for file in glob.glob(dir+"/*"):

                                if os.path.isfile(file):
                                        open_file(file)
                                if os.path.isdir(file):
                                        open_folder(file)

