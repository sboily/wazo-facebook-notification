Plugin for configure facebook notification

	git clone https://github.com/sboily/wazo-facebook-notification
	cd wazo-facebook-notification
	pip install -r requirements.txt
	pip3 install -r requirements.txt
	python setup.py install
	python3 setup.py install
        cp -a /etc/facebook /etc
        chown wazo-admin-ui.wazo-admin-ui /etc/facebook/*
	cp etc/wazo-admin-ui/conf.d/* /etc/wazo-admin-ui/conf.d
	cp etc/wazo-webhookd/conf.d/* /etc/wazo-webhookd/conf.d
	systemctl restart wazo-admin-ui
	systemctl restart wazo-webhookd
