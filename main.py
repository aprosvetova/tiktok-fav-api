from aiohttp import web
from TikTokApi import TikTokApi
from TikTokApi.browser import custom_options, set_async

set_async()
custom_options({
    'args': ['--no-sandbox', '--disable-gpu'],
    'executablePath': '/usr/bin/chromium-browser'
})

api = TikTokApi()


async def get_liked(request):
    username = request.match_info.get('username')
    try:
        likes = api.userLikedbyUsername(username)
        return web.json_response({'likes': [v['id'] for v in likes]})
    except Exception as e:
        return web.json_response({'error': repr(e)}), 500


app = web.Application()
app.add_routes([web.get('/user/{username}', get_liked)])

web.run_app(app)
