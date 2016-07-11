from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from sitetree.sitetreeapp import register_i18n_trees

admin.autodiscover()

import symposion.views
import pycon.profile.views

# from pinax.apps.account.openid_consumer import PinaxConsumer


URL_PREFIX = settings.CONFERENCE_URL_PREFIXES[settings.CONFERENCE_ID]


def gen_urls():
    include_patterns = patterns("",
                                url(r"^$", TemplateView.as_view(template_name="homepage.html"),
                                    name="home"),
                                url(r"^admin/", include(admin.site.urls)),
                                url(r"^account/signup/$", pycon.profile.views.SignupView.as_view(),
                                    name="account_signup"),
                                url(r"^account/login/$", symposion.views.LoginView.as_view(), name="account_login"),
                                url(r"^account/social/", include("social_auth.urls")),
                                url(r"^account/associations/", include("symposion.social_auth.urls")),
                                url(r"^account/", include("account.urls")),
                                url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),
                                url(r"^blog/", include("biblion.urls")),
                                url(r"^force500/", lambda request: xxx),
                                url(r"^registration/", include("pycon.registration.urls")),
                                url(r"^finaid/", include("pycon.finaid.urls")),
                                url(r"^pycon_api/", include("pycon.pycon_api.urls")),
                                url(r"^api/", include("pycon.apis.urls")),
                                url(r"^schedule/", include("pycon.schedule.urls")),
                                url(r"^profile/", include("pycon.profile.urls")),
                                url(r"^tutorials/", include("pycon.tutorials.urls")),

                                url(r"^speaker/", include("symposion.speakers.urls")),
                                url(r"^proposals/", include("pycon.proposals.urls")),
                                url(r"^reviews/", include("symposion.reviews.urls")),
                                url(r"^teams/", include("symposion.teams.urls")),
                                url(r"^schedule/", include("symposion.schedule.urls")),
                                url(r"^conference/", include("symposion.conference.urls")),

                                url(r"^sponsors/", include("pycon.sponsorship.urls")),

                                url(r"^boxes/", include("symposion.boxes.urls")),
                                url(r"^sitemap/", TemplateView.as_view(template_name="static/sitemap.html"),
                                    name="sitemap"),
                                url(r'^selectable/', include('selectable.urls')),
                                url(r"^change_language/", symposion.views.change_language, name="change_language"),
                                url(r"^", include("pycon.urls")),

                                # This should be last, because it will create a new CMS page for
                                # any unrecognized URL.
                                url(r"^", include("restcms.urls")),
                                url(r'^localeurl/', include('localeurlcustom.urls')),
    )

    for key, val in settings.LANGUAGES:
        yield url(r"^%s/%s/" % (URL_PREFIX, key), include(include_patterns))

urlpatterns = patterns("",
                       url(r"^$", RedirectView.as_view(url="/%s/" % URL_PREFIX, permanent=False) ),
                       *[gen for gen in gen_urls()]
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# pycon site uses "main" sitetree. so the name of internationalized one must_be "main_${lang_code}"
register_i18n_trees(['main'])
