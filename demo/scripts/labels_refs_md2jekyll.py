
def minimal_ordered_set(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def get_labels_tags_dic(labels_pattern, doc_lines):
    COUNTER = 0
    labels_tags_all = []

    for line in doc_lines:
        labels_matched_raw = re.findall(labels_pattern, line)
        if labels_matched_raw:
            COUNTER +=1
            labels_tags = [s.translate({ord(i): None for i in strings_for_removal}) for s in labels_matched_raw]
            labels_tags = list(minimal_ordered_set(labels_tags))
            labels_tags_all += labels_tags

    #############################################
    # Test for non-repeated labels
    #############################################
    if COUNTER == len(labels_tags_all):
        print("Good! There aren't repeated labels in your file")
        labels_tags_dic = {labels_tags_all[n]:str(n+1) for n in range(COUNTER)}
        return labels_tags_dic
    else:
        print("There are repeated labels in your file. This will lead to errors")

def replace_ref_syntax(refs_matched_raw, line):
    refs_tags = [s.translate({ord(i): None for i in strings_for_removal}) for s in refs_matched_raw]
    refs_tags = list(set(refs_tags))
    #############################################
    # Replace Markdown reference syntax
    #############################################
    line_modified = line
    for x in refs_tags:
        chunk_original = '@'+marker+':'+x
        x_number = labels_tags_dic[x]
        chunk_new = '['+marker+':'+x_number+'](#'+x+')'
        line_modified = line_modified.replace(chunk_original, chunk_new)
    
    return line_modified
    
def replace_label_syntax(labels_matched_raw, line):
    labels_tags = [s.translate({ord(i): None for i in strings_for_removal}) for s in labels_matched_raw]
    labels_tags = list(set(labels_tags))
    #############################################
    # Replace Markdown reference syntax
    #############################################    
    for x in labels_tags:
        chunk_original = '{#'+marker+':'+x+'}'
        chunk_new = '\n<a id="'+x+'"></a>'
        line_modified = re.sub(r'\{#'+marker+':'+x+'(.+?)\}', chunk_new, line)
    
    return line_modified

def markdown_to_jekyll_labels_refs_V1(doc_lines, md_outfile):
    with open(md_outfile,'w') as doc_outfile:
        for line in doc_lines:
            refs_matched_raw = re.findall(refs_pattern,line)
            labels_matched_raw = re.findall(labels_pattern, line)

            if refs_matched_raw and not labels_matched_raw:
                line_modified = replace_ref_syntax(refs_matched_raw, line)
                doc_outfile.write(line_modified)

            elif labels_matched_raw and not refs_matched_raw:
                line_modified = replace_label_syntax(labels_matched_raw, line)
                doc_outfile.write(line_modified)

            elif labels_matched_raw and refs_matched_raw:
                line_modified = replace_label_syntax(labels_matched_raw, line)
                line_modified = replace_ref_syntax(refs_matched_raw, line_modified)
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

    labels_pattern = re.compile('#'+marker+'(.+?)\s')
    refs_pattern = re.compile('@'+marker+'(.+?)\s')
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
        labels_tags_dic = get_labels_tags_dic(labels_pattern, doc_lines)
        markdown_to_jekyll_labels_refs_V1(doc_lines, md_outfile)
    except:
        print("Couldn't find Markdown file. Check your input path")
