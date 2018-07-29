from django.http import JsonResponse

class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     if self.request.is_ajax():
    #         data = {
    #             'pk': self.object.pk,
    #         }
    #         return JsonResponse(data)
    #     else:
    #         return response