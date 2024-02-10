from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Comment
from webapp.forms import CommentForm
from django.urls import reverse

def add_comment(request, advertisement_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.advertisement_id = advertisement_id
            comment.save()
            return redirect('webapp:advertisement_detail', pk=advertisement_id)
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form})


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.author:
        comment.delete()
    return redirect('webapp:advertisement_detail', pk=comment.advertisement_id)

