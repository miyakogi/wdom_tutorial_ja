#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from wdom.misc import install_asyncio # tornadoを使う時だけ必要です
from wdom.server import get_app, start_server, stop_server
from wdom.document import get_document


if __name__ == '__main__':
    install_asyncio() # tornadoを使う時だけ必要です

    document = get_document()
    h1 = document.createElement('h1')
    h1.textContent = 'Hello, WDOM'
    def rev_text(event):
        # h1の中身の文字列を反転
        h1.textContent = h1.textContent[::-1]
    h1.addEventListener('click', rev_text)
    document.body.appendChild(h1)

    app = get_app(document)
    loop = asyncio.get_event_loop()
    server = start_server(app, port=8888, loop=loop)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        stop_server(server)
