from django.shortcuts import render, get_object_or_404
from .models import DiaryEntry
from .forms import DiaryEntryForm
from django.shortcuts import redirect


def entry_list(request):
    entries = DiaryEntry.objects.all()
    return render(request, 'diary/entry_list.html', {'entries': entries})


def entry_detail(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk)
    return render(request, 'diary/entry_detail.html', {'entry': entry})


def entry_new(request):
    if request.method == "POST":
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/entry_edit.html', {'form': form})


def entry_edit(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk)
    if request.method == "POST":
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'diary/entry_edit.html', {'form': form})


def entry_delete(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk)
    entry.delete()
    return redirect('entry_list')
