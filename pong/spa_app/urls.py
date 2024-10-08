from django.urls import path
from .views import (
    # Authentication Views
    LoginView, 
    SignupView, 
    VerifyEmailView,
    PasswordResetView, 
    ValidateTokenView, 
    SetNewPasswordView, 

    # Profile Views
    BaseTemplateView,
    EditProfileView,
    UserDataView,
    
    # Friend Request Views
    SendFriendRequestView, 
    AcceptFriendRequestView, 
    GetFriendRequestsView, 
    GetFriendsView, 
    RejectFriendRequestView,

    # CSRF Token
    FetchCSRFTokenView,

    #Status on off
    UpdateStatusView,

    # Chat
    MessagesListView,
    SendMessageView,
    GameHistoryView,

    # Logout
    LogoutView,
    CheckAuthenticationView,
    FriendProfileView,

    # Block
    UnblockUserView,
    BlockUserView,
    CheckBlockStatusView,

    # 42OAuth
    OAuthConfigView,
    Auth42CallbackView,
    TokenRefreshView,

    # 2FA
    Verify2FAView,
    Enable2FAView,
    Verify2FALView,
    Get2FAStatusView,
    RequestDisable2FACodeView, 
    VerifyDisable2FAView
)


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BaseTemplateView.as_view(), name='base'),
    path('api/check-authentication/', CheckAuthenticationView.as_view(), name='check_authentication'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('fetch-csrf-token/', FetchCSRFTokenView.as_view(), name='fetch_csrf_token'),
    path('email-verify/<uidb64>/<token>/', VerifyEmailView.as_view(), name='email_verify'),
    path('api/user-data/', UserDataView.as_view(), name='user_data'),
    path('api/password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/validate-token/', ValidateTokenView.as_view(), name='validate_token'),
    path('api/set-new-password/', SetNewPasswordView.as_view(), name='set_new_password'),
    path('api/edit-profile/', EditProfileView.as_view(), name='edit-profile'),
    path('send-friend-request/', SendFriendRequestView.as_view(), name='send_friend_request'),
    path('accept-friend-request/<int:request_id>/', AcceptFriendRequestView.as_view(), name='accept_friend_request'),
    path('get-friend-requests/', GetFriendRequestsView.as_view(), name='get_friend_requests'),
    path('reject-friend-request/<int:request_id>/', RejectFriendRequestView.as_view(), name='reject_friend_request'),
    path('get-friends/', GetFriendsView.as_view(), name='get_friends'),
    path('api/messages/<str:username>/', MessagesListView.as_view(), name='messages-list'),
    path('api/message/send/', SendMessageView.as_view(), name='send-message'),
    path('api/game-history/', GameHistoryView.as_view(), name='game-history'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/friend-profile/<str:username>/', FriendProfileView.as_view(), name='friend-profile'),
    path('update-status/', UpdateStatusView.as_view(), name='update_status'),
    path('block/<str:friend_username>/', BlockUserView.as_view(), name='block_user'),
    path('unblock/<str:friend_username>/', UnblockUserView.as_view(), name='unblock_user'),
    path('api/oauth/config/', OAuthConfigView.as_view(), name='oauth_config'),
    path('auth42/', Auth42CallbackView.as_view(), name='auth42_callback'),
    path('api/check-block-status/<str:username>/', CheckBlockStatusView.as_view(), name='check_block_status'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('enable-2fa/', Enable2FAView.as_view(), name='enable_2fa'),
    path('verify-2fa/', Verify2FAView.as_view(), name='verify_2fa'),
    path('verify-2fal/', Verify2FALView.as_view(), name='verify_2fal'),
    path('get-2fa-status/', Get2FAStatusView.as_view(), name='get_2fa_status'),
    path('request-disable-2fa-code/', RequestDisable2FACodeView.as_view(), name='request_disable_2fa_code'),
    path('verify-disable-2fa/', VerifyDisable2FAView.as_view(), name='verify_disable_2fa'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
