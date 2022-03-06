from django.conf import settings
from core.ct_api import CrowdTangleAPI


class IGCrowdTangleAPI(CrowdTangleAPI):
    TOKEN = (settings.CROWDTANGLE_INSTAGRAM_API_KEY,)
