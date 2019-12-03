
def replace_caption_syntax(captions_matched_raw, item):
    caption = captions_matched_raw[0]
    html_syntax_items = (
        '<figcaption style="text-align:center;font-size:14px">',
        '<b>latex_marker:latex_label </b>',
        '<em>'+' ',
        caption,
        '</em>',
        '</figcaption>'
    )
    chunk_new = ''.join(html_syntax_items)
    chunk_original = r'\caption{'+caption+'}'
    item_modified = item.replace(chunk_original, chunk_new)
    return item_modified

def latex_to_html_captions(nb, nb_outfile):
    for i in range(len(nb['cells'])):
        cell = nb['cells'][i]
        for j in range(len(cell['source'])):
            item = cell['source'][j]

            captions_matched_raw = re.findall(captions_pattern,item)
            if captions_matched_raw:
                item_modified = replace_caption_syntax(captions_matched_raw, item)
                nb['cells'][i]['source'][j] = item_modified

    #############################################
    # Modify cell content with new syntax accordingly
    #############################################
    with open(nb_outfile,'w') as fp:
        json.dump(nb, fp)
    fp.close()
    print("New Notebook successfully generated")
    

if __name__ == "__main__":
    import re
    import sys
    import json
    #############################################
    # Settings
    #############################################
    captions_pattern = re.compile(r'\\caption\{(.+?)\}')
    #############################################
    # Script input arguments (self-explanatory)
    #############################################
    nb_infile = sys.argv[1]
    nb_outfile = sys.argv[2]
    #############################################
    # Load Jupyter Notebook as Dictionary
    #############################################
    try:
        with open(nb_infile,'r') as fp:
            nb = json.load(fp)
        fp.close()
        #############################################
        # Turn LaTeX label/ref syntax in Jupyter Noteboks into MD syntax
        #############################################
        latex_to_html_captions(nb, nb_outfile)
    except:
        print("Couldn't find Jupyter Notebook. Check your input path")
