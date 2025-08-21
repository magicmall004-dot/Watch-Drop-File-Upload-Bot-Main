# ==============================================================
# Watch Drop Bot - Init
# Copyright (c) 2025 Watch Drop
# Licensed under the MIT License
# ==============================================================

from aiohttp import web
from .route import routes

async def web_server():
    """Initialize and return aiohttp web server with routes"""
    web_app = web.Application(client_max_size=30_000_000)
    web_app.add_routes(routes)
    return web_app
