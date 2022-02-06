import string
import re
inc_str = r'''homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

try:
    # convert all text to lowercase
    inc_str = inc_str.lower()

    word_from = 'iz'
    word_to = 'is'
    spc = ' '
    # some replaces
    inc_str = inc_str.replace(spc + word_from + spc, spc + word_to + spc).replace(' tex.', ' text.').replace('\n\n', '\n')
except:
    print('\nError 1 occurs.')

try:
    # convert letter after :(colon) to capital
    # [\D\S]  matches any character, digit, whitespace or otherwise.
    list_colon_inside = re.findall(r'[\D\S]:[\s]+\w?', inc_str)
    for y in range(len(list_colon_inside)):
        repl_from = str(list_colon_inside[y])
        repl_to = repl_from[:-1] + repl_from[-1].upper()
        inc_str = inc_str.replace(repl_from, repl_to)
except:
    print('\nError 2 occurs.')

try:
    # add space before “ in Fix“iz”
    list_quot_inside = re.findall(r'\S“.*?”', inc_str)
    for y in range(len(list_quot_inside)):
        repl_from = str(list_quot_inside[y])
        repl_to = repl_from[0] + spc + repl_from[1:]
        inc_str = inc_str.replace(repl_from, repl_to)
except:
    print('\nError 3 occurs.')

try:
    # generate new sentence from last words of each existing sentence
    sent_new = []
    for word in inc_str.split():
        if word[-1] == '.':
            sent_new.append(word[:-1])
    if len(sent_new) > 0:
        sent_new[0] = sent_new[0].capitalize()
    nice_sent_add = ' '.join(sent_new) + '.'
except:
    print('\nError 4 occurs.')

final_text = ''
try:
    # split  into paragraphs
    par_list = inc_str.split('\n\n')
    list_nice_sent = []
    for p in range(len(par_list)):
        par = par_list[p]
        # split into sentences
        inc_str_list_sent = par.split('.')
        # count the number of sentences in a paragraph (split provides an additional sentence [])
        real_num_sent = 0
        for n in range(len(inc_str_list_sent)):
            # if inc_str_list_sent[n] is not empty
            if inc_str_list_sent[n]:
                # enumerator increment
                real_num_sent += 1

        for i in range(real_num_sent):
            # if inc_str_list_sent[i] is not empty
            if inc_str_list_sent[i]:
                # find the first word and capitalize it
                first_word = inc_str_list_sent[i].split()[0].capitalize()
                # processing when the first word has :(colon)
                if first_word[-1] == ':':
                    first_word = first_word + '\n'
                # split sentence into words and create raw sentence from them
                # concatenating a list of words using space
                sent = ' '.join(inc_str_list_sent[i].split())
                # create a correct sentence from the first word and  the rest of the sentence
                nice_sent = ''.join(first_word + sent[len(first_word):] + '. ')

                # add nice sentence into 'list_nice_sent' list
                list_nice_sent.append(nice_sent)

                # add new sentence to the end od second paragraph
                if p == 1 and real_num_sent - 1 == i:
                    list_nice_sent.append(nice_sent_add)
                # add \n after last sentence of paragraph
                if real_num_sent - 1 == i:
                    list_nice_sent.append('\n')

    # generate a final result concatenating a list of strings (nice sentences) using '' and remove spaces from the right
    final_text = ''.join(list_nice_sent).rstrip()
except:
    print('\nError 5 occurs.')

try:
    # calculate number of whitespace in a text
    numb_wspc = len(re.findall(r'\s', final_text))
    # display final text
    print(f'\nFinal result:\n\n{final_text}')
    # display umber of whitespaces
    print(f'\nNumber of whitespace characters in this text is {numb_wspc}.')
except:
    print('\nError 6 occurs.')