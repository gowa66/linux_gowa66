from django.conf import settings
from portfolio.models import *
from portfolio.forms import *

from mcbv.detail import DetailView
from mcbv.list import ListView
from mcbv.list_custom import ListRelated, DetailListFormSetView
from mcbv.edit_custom import FormSetView, UpdateView

from shared.utils import *


class Main(ListView):
    list_model    = Group
    paginate_by   = 10
    template_name = "portfolio/list.html"

class SlideshowView(ListRelated):
    list_model    = Image
    detail_model  = Group
    related_name  = "images"
    template_name = "portfolio/slideshow.html"


class GroupView(DetailListFormSetView):
    """List of images in an group, optionally with a formset to update image data."""
    detail_model       = Group
    formset_model      = Image
    formset_form_class = ImageForm
    related_name       = "images"
    paginate_by        = 25
    template_name      = "portfolio/group.html"

    def add_context(self):
        return dict( show=self.kwargs.get("show", "thumbnails") )

    def process_form(self, form):
        if self.user.is_authenticated(): form.save()

    def get_success_url(self):
        return "%s?%s" % (self.detail_absolute_url(), self.request.GET.urlencode()) # keep page num


class AddImages(DetailView, FormSetView):
    """Add images to a group view."""
    detail_model       = Group
    formset_model      = Image
    formset_form_class = AddImageForm
    template_name      = "portfolio/add_images.html"
    extra              = 10

    def process_form(self, form):
        form.instance.update( group=self.get_detail_object() )

    def get_success_url(self):
        return self.detail_absolute_url()


class ImageView(UpdateView):
    form_model      = Image
    modelform_class = ImageForm
    template_name   = "portfolio/image.html"

    def form_valid(self, form):
        if self.user.is_authenticated(): form.save()

    def edit(self):
        return self.user.is_authenticated() and self.request.GET.get("edit")


def portfolio_context(request):
    return dict(user=request.user, media_url=settings.MEDIA_URL)
