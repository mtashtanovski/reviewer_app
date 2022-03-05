from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review/review_add.html'
    form_class = ReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('webapp:product_view', pk=product.pk)


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_update.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={"pk": self.object.product.pk})


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_delete.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={"pk": self.object.product.pk})
