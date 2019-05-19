
install:	# Run as sudo
	#add-apt-repository ppa:chris-lea/node.js
	#apt-get update
	apt-get install nodejs npm -y
	npm install -g node-gyp
interface:
	swig -javascript -node -c++ dice.i
	node-gyp configure
	node-gyp build
test:
	node test.js
