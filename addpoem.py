"""
List of markdown things for porm:
<b> </b> will be made bold
<i> </i> italics
<u> </u> underline
<t> </t> title (bold and big)
<r> </r> align right (align left by default)
<m> </m> align middle

Title supplied to script will be applied automatically, or you can leave it blank
and do it in the txt file (not recommended). Be aware that this program will not do any error checking
for you. space as you desire.
"""

markup = {
    "<b>": "<span class='bold'>",
    "<i>": "<span class='italicize'>",
    "<u>": "<span class='underline'>",
    "<t>": "<span class='poemtitle'>",
    "<r>": "<span class='poemright'>",
    "<m>": "<span class='poemmiddle'>",
    "</b>": "</span>",
    "</u>": "</span>",
    "</i>": "</span>",
    "</r>": "</span>",
    "</t>": "</span>",
    "</m>": "</span>",
}

choice = input("Enter 0 to add a poem, 1 to remove a poem.\n")
if choice=='0':
    poem = open("addpoem.txt",'r').read()
    print("Poem read.")

    if "__TITLE__" in poem:
        print("BADBABABDBABBAD")
        quit()

    title = input("Enter poem title:\n")

    toappend=["__TITLE__",title,'\n']
    for m in markup:
        poem.replace(m,markup[m])
    for char in poem:
        if char==' ':
            toappend.append('&nbsp;')
        elif char=='\n':
            toappend.append('<br>')
        else:
            toappend.append(char)
    file = open("poems.txt",'a')
    file.write("".join(toappend))
    file.close()
    print("Done.")
else:
    print("WARNING: This program will delete all poems with the title you supply. It is not case sensitive.")
    title = input("Title of poem you would like to remove:\n").lower()

    poems = open("poems.txt",'r').read()

    poemlist = poems.split('__TITLE__')
    newpoemlist=[]
    count=0
    for poem in poemlist:
        if poem.split('\n')[0].lower != title:
            newpoemlist.append(poem)
        else:
            print("Poem removed.")
            count+=1
    file = open("poems.txt",'w')
    file.write("__TITLE__".join(newpoemlist))
    file.close()
    print("Done. Removed ",count," poems.")
        

