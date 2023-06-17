title: whisper on the edge
date: 2023-06-17
Modified: 2023-06-17
Tags: dictationPI
Slug: early stage research into edge dictation
Authors: clexp
Summary: <img align="left" width="100" height="100" src=/images/#.jpg>Ideas and what is out there




I am sure I am not alone in having more ideas than I can work with. But it helps when I am looking at new projects.
### The itch
I wanted some sort of dictation tool that I can speak freely into. I wanted it to behave like a keyboard. This means I can use it anywhere. I speak into it and it sends a string of characters just like a keyboard. I have learnt this is possible using the key remapper. I have seen that the dictation is possible on the desktop. I wondered if I could have some sort of dictation and set that would simply send characters to the USB port. This would improve brackets possibly) the dictation speed and would not be bound in the same way that Microsoft Word is. Namely, cutting and pasting between documents. It could also be trained on my voice as I would take it with me. It would not be in the cloud so I would have no patient data concerns.

### What's out there.
There are lots of dictation services out there. Here are a few bullet list analyst AI lexicon. But are there any IOT projects. Well, recently open AI released whisper. This is a local only speech recognition tool. It was then re-compiled to a C++ module so it can run on a CPU chip, not a GPU. The YouTube videos indicate people get good results with this. There is some indication it has even been run on a raspberry pie. So now there are hardware options, software, options, and more. It seems a few people have even done this themselves.

Quite a few of the tools out there are limited to 2 or 300 words. This is not quite what I want if I am doing medical dictation. However, the range of speech is comparatively limited compared to full English. And the device would not need to be universally trained on my voice.

Interestingly, whisper is built on many (30?) Layers of transformers. However, it now seems you can use, just two layers with some other architectural layers instead. Having listened to this podcast, TWIML, I might be able to get higher speed and higher accuracy with a different model. But where is this model?

