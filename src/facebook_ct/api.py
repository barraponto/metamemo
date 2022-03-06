from django.conf import settings
from core.ct_api import CrowdTangleAPI


class FBCrowdTangleAPI(CrowdTangleAPI):
    TOKEN = settings.CROWDTANGLE_FACEBOOK_API_KEY
