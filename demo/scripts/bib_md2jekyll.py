
def markdown_to_jekyll_bib(md_infile, md_outfile, bib_filename):
    #############################################
    # Extract all lines from input MD file
    #############################################
    try:
        doc_infile = open(md_infile, 'r')
        doc_lines = doc_infile.readlines()
    except:
        print("Couldn't find Markdown file. Check your input path")

    with open(md_outfile, 'w') as doc_outfile:
        for line in doc_lines:
            #############################################
            # Filter all lines containing bibliography syntax
            #############################################
            line_matched = re.search(r'\[@(.+?)\]',line)
            if line_matched:
                #############################################
                # Extract Bib tags from substrings in filtered lines
                #############################################
                chunk_matched = line_matched.group(1)
                bib_tags_raw = re.split(";|,", chunk_matched)
                bib_tags_clean = [x.replace("@",'').strip() for x in bib_tags_raw]
                #############################################
                # Replace Markdown syntax with jekyll's in filtered lines
                #############################################
                jekyll_syntax_items = ["{% cite"]+bib_tags_clean+['--file '+bib_filename]+["%}"]
                separator = ' '
                chunk_new = separator.join(jekyll_syntax_items)
                chunk_original = '[@'+chunk_matched+']'
                line_modified = line.replace(chunk_original, chunk_new)
                #############################################
                # Write syntax modified line in output file
                #############################################
                doc_outfile.write(line_modified)
            else:
                doc_outfile.write(line)
        #############################################
        # Add jekyll line to generate list of references at document end
        #############################################        
        bib_endline = "\n{% bibliography --file "+bib_filename+" --cited %}"
        doc_outfile.write(bib_endline)
        # Close all files
        doc_infile.close()
        doc_outfile.close()

if __name__ == "__main__":
    import sys
    import re
    #############################################
    # Script input arguments (self-explanatory)
    #############################################
    md_infile = sys.argv[1]
    md_outfile = sys.argv[2]
    bib_filename = sys.argv[3]
    #############################################
    # Turn MD file into jekyll-syntax modified file
    #############################################
    markdown_to_jekyll_bib(md_infile, md_outfile, bib_filename)
