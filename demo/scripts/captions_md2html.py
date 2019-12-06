def replace_caption_syntax(captions_matched_raw, line):
    caption = captions_matched_raw[0]
    html_syntax_items = (
        '<figcaption style="text-align:center;font-size:14px">',
        '<b>',
        marker+':latex_label ',
        '</b>',
        '<em>'+' ',
        caption,
        '</em>',
        '</figcaption>'
    )
    chunk_new = ''.join(html_syntax_items)
    return line+chunk_new

def markdown_to_html_captions(doc_lines, md_outfile):
    with open(md_outfile,'w') as doc_outfile:
        for line in doc_lines:
            captions_matched_raw = re.findall(captions_pattern,line)
            labels_matched_raw = re.findall(captions_pattern,line)
            if captions_matched_raw:
                line_modified = replace_caption_syntax(captions_matched_raw, line)
                doc_outfile.write(line_modified)
            else:
                line_modified = line
                doc_outfile.write(line_modified)
        doc_outfile.close()
        print("New Markdown file successfully generated!")
    
if __name__ == "__main__":
    import re
    import sys
    #############################################
    # Settings
    #############################################
    marker = 'fig'
    strings_for_removal = ').,;:'
    
    captions_pattern = re.compile(r'!\[(.+?)\]')
    labels_pattern = re.compile('#'+marker+'(.+?)\s')
    #############################################
    # Script input arguments (self-explanatory)
    #############################################
    md_infile = sys.argv[1]
    md_outfile = sys.argv[2]
    #############################################
    # Extract all lines from input MD file
    #############################################
    try:
        doc_infile = open(md_infile, 'r')
        doc_lines = doc_infile.readlines()
        doc_infile.close()
        #############################################
        # Turn MD file into jekyll-syntax modified file
        #############################################
        markdown_to_html_captions(doc_lines, md_outfile)
    except:
        print("Couldn't find Markdown file. Check your input path")
