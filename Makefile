build : requirements.txt
	test `which pip` || easy_install pip
	test `which virtualenv-2.7` || sudo pip install virtualenv
	test -d venv || virtualenv-2.7 --system-site-packages venv
	source venv/bin/activate; pip install -r requirements.txt
	touch venv/bin/activate









use_nginx: 
	mkdir server && mkdir server/nginx && cd server/nginx && \
	wget http://sourceforge.net/projects/pcre/files/pcre/4.4/pcre-4.4.tar.gz/download -O pcre.tar.gz &&\
	wget http://zlib.net/zlib-1.2.8.tar.gz -O zlib.tar.gz && \
	wget http://nginx.org/download/nginx-1.4.6.tar.gz -O nginx.tar.gz && \
	tar -zxvf pcre.tar.gz && \
	tar -zxvf zlib.tar.gz && \
	tar -zxvf nginx.tar.gz && \
	cd nginx-1.4.6 && \
	./configure --prefix=../ --with-pcre=../pcre-4.4 --with-zlib=../zlib-1.2.8 && \
	make && \
	make install;
	cd server/nginx && rm -rf *.tar.gz zlib-1.2.8 pcre-4.4;
	


	
	

	
	
	
	
	
	
	
construct : bin/createdb.sh venv
	source venv/bin/activate;
	##makeing deployment server 
	django-admin.py startproject lncrnadb_deployment
	mkdir ./lncrnadb_deployment/static 	
	sh bin/createdb.sh lncrnadb_deployment root ${dbpass}
	cp -f ./config/deployment_settings.py ./lncrnadb_deployment/lncrnadb_deployment/settings.py
	#makign production server
	django-admin.py startproject lncrnadb_production 
	sh bin/createdb.sh lncrnadb_production root ${dbpass}
	cp -f ./config/production_settings.py ./lncrnadb_production/lncrnadb_production/settings.py
	


	
remove_construct: lncrnadb_deployment lncrnadb_production
	rm -rf lncrnadb_production
	rm -rf lncrnadb_deployment
	
production: lncrnadb_production/
	gunicorn -D lncrnadb_production.wsgi:application

deployment: lncrnadb_deployment/
	gunicorn --D lncrnadb_deployment.wsgi:application
	


update:
	source venv/bin/activate; pip install -Ur requirements.txt
	
	
clean:
	rm -rf venv
	rm -rf lncrnadb
	rm -rf lncrnadb_deployment
	rm -rf lncrnadb_production
	rm -rf ./config/*.conf
	rm -rf server
	