PREFIX = /usr

all:

install:
	install -Dm644 index.theme ${DESTDIR}${PREFIX}/share/sounds/borealis/index.theme
	install -Dm644 stereo.index ${DESTDIR}${PREFIX}/share/sounds/borealis/stereo.index
	cp -r stereo ${DESTDIR}${PREFIX}/share/sounds/borealis
