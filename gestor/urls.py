"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import cost
from .views import dashboard
from .views import reports
from gestor.tools.week_stats_recal import initRecalculator
from rbac.init_permissions import init_permissions


def trigger_error(request):
    pass


initRecalculator()


urlpatterns = [
    path("sentry-debug/", trigger_error),
    path("admin/", admin.site.urls),
    path("", dashboard.dashboard, name="dashboard"),
    # Weekly reports
    path("weekly/", reports.weekly_report, name="weekly-report"),
    path("weekly/<date>", reports.weekly_report, name="weekly-report-date"),
    path(
        "weekly/<category_id>/<date>",
        reports.weekly_payments,
        name="weekly-payments",
    ),
    path(
        "weekly_membership/",
        reports.weekly_membership_report,
        name="weekly-membership",
    ),
    path(
        "weekly_membership/<date>",
        reports.weekly_membership_report,
        name="weekly-membership-date",
    ),
    path(
        "week-stats-recalculate/<date>",
        dashboard.week_stats_recalculate,
        name="week-stats-recalculate",
    ),
    path("weekly-costs/<category_id>/<date>",
         cost.weekly_cost, name="weekly-cost"),
    # Monthly reports
    path("monthly/", reports.monthly_report, name="monthly-report"),
    path(
        "monthly/<year>/<month>", reports.monthly_report, name="monthly-report-date"
    ),
    path(
        "monthly/<category_id>/<year>/<month>",
        reports.monthly_payments,
        name="monthly-payments",
    ),
    path(
        "monthly_membership/",
        reports.monthly_membership_report,
        name="monthly-membership",
    ),
    path(
        "monthly_membership/<year>/<month>",
        reports.monthly_membership_report,
        name="monthly-membership-date",
    ),
    path(
        "monthly-costs/<category_id>/<year>/<month>",
        cost.monthly_cost,
        name="monthly-cost",
    ),
    # Apps
    path("users/", include("users.urls")),
    path("inventory/", include("inventory.urls")),
    path("services/", include("services.urls")),
    path("equipment/", include("equipment.urls")),
    path("costs/", include("costs.urls")),
    path("rent/", include("rent.urls")),
    path("utils/", include("utils.urls")),
    path("tolls/", include("tolls.urls")),
    path("template/", include("template_admin.urls")),
    path("rbac/", include("rbac.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


init_permissions()
