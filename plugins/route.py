# +++ Made By Sanjiii [telegram username: @Urr_Sanjiii] +++

from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Raven Premium Bot")

# +++ Made By Sanjiii [telegram username: @Urr_Sanjiii] +++