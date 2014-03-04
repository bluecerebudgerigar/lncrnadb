build : requirements.txt
	
	test `which pip` || easy_install pip
	test `which virtualenv-2.7` || sudo pip install virtualenv
	test -d venv || virtualenv-2.7 -p --system=site-packages venv
	source venv/bin/activate; pip install -r requirements.txt
	touch venv/bin/activate
	
	
construct : 
	source venv/bin/activate; 
	django-admin.py startproject lncrnadb;
	


update:
	source venv/bin/activate; pip install -Ur requirements.txt
	
	
clean:
	rm -rf venv
	