from django.shortcuts import render


def word_counter(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        word_count = len(text.split())
        return render(request, 'counter/word_counter.html', {
            'text': text,
            'word_count': word_count
        })
    return render(request, 'counter/word_counter.html')
