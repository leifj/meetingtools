from django.conf.urls.defaults import patterns,include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from meetingtools.settings import ADMIN_MEDIA_ROOT, MEDIA_ROOT, STATIC_ROOT
from meetingtools.multiresponse import redirect_to
from meetingtools.apps.room.feeds import RoomAtomTagFeed,RoomRSSTagField,\
    AtomRecordingFeed, RSSRecordingField
admin.autodiscover()

def welcome(request):
    return redirect_to('/rooms')

urlpatterns = patterns('',
    (r'^$',welcome),
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': STATIC_ROOT}),
    # Login/Logout
    (r'^accounts/login?$','meetingtools.apps.auth.views.login'),
    (r'^accounts/login-federated$','meetingtools.apps.auth.views.accounts_login_federated'),
    (r'^accounts/logout$','meetingtools.apps.auth.views.logout'),
    (r'^user/?(.*)$','meetingtools.apps.room.views.list_rooms'),
    (r'^(?:room|rooms)$','meetingtools.apps.room.views.list_rooms'),
    (r'^go/(\d+)$','meetingtools.apps.room.views.go_by_id'),
    (r'^go/(.+)$','meetingtools.apps.room.views.go_by_path'),
    (r'^launch/(\d+)$','meetingtools.apps.room.views.launch'),
    (r'^promote/(\d+)$','meetingtools.apps.room.views.promote_and_launch'),
    (r'^room/create$','meetingtools.apps.room.views.create'),
    (r'^room/(\d+)$','meetingtools.apps.room.views.view'),
    (r'^room/(\d+)/modify$','meetingtools.apps.room.views.update'),
    (r'^room/(\d+)/delete$','meetingtools.apps.room.views.delete'),
    (r'^room/(\d+)/unlock$','meetingtools.apps.room.views.unlock'),
    (r'^room/(\d+)/tag$','meetingtools.apps.room.views.tag'),
    (r'^room/(\d+)/untag/(.+)$','meetingtools.apps.room.views.untag'),
    (r'^room/(\d+)/recordings$','meetingtools.apps.room.views.recordings'),
    (r'^room/\+(.+)\.(?:json|html|htm)$','meetingtools.apps.room.views.list_by_tag'),
    (r'^room/\+(.+)\.(?:atom)$',RoomAtomTagFeed()),
    (r'^room/\+(.+)\.(?:rss)$',RoomRSSTagField()),
    (r'^room/(\d+)/recordings\.(?:atom)$',AtomRecordingFeed()),
    (r'^room/(\d+)/recordings\.(?:rss)$',RSSRecordingField()),
    (r'^room/\+(.+)$','meetingtools.apps.room.views.list_by_tag'),
    (r'^widget/?\+?(.*)$','meetingtools.apps.room.views.widget'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^api/stats/user/(.*)$','meetingtools.apps.stats.views.user_minutes_api'),
    (r'^api/stats/domain/(.+)$','meetingtools.apps.stats.views.domain_minutes_api'),
    (r'^api/stats/room/(\d+)$','meetingtools.apps.stats.views.room_minutes_api'),
    (r'^api/room/(\d+)/occupation$','meetingtools.apps.room.views.occupation'),
    (r'^stats$','meetingtools.apps.stats.views.user'),
    (r'^stats/user/(.+)$','meetingtools.apps.stats.views.user'),
    (r'^stats/domain/(.+)$','meetingtools.apps.stats.views.domain'),
    (r'^stats/room/(\d+)$','meetingtools.apps.stats.views.room'),
)
