import os
import re

def fix_github_links_in_html():
    """Fix GitHub repository links to point to Jekyll-processed pages instead"""
    
    vault_dir = r"c:\Users\WORK_ADMIN\Documents\Obsidian Vault"
    
    # Pattern to match GitHub repository URLs
    github_pattern = r'https://github\.com/StudioCordillera/math1414-obsidian-vault/blob/main/(.*?)\.md'
    
    count = 0
    for root, dirs, files in os.walk(vault_dir):
        for file in files:
            if file.endswith('.html') and file != 'index.html':  # Skip the main index
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Check if file contains GitHub links
                    if 'github.com/StudioCordillera' in content:
                        # Replace GitHub links with Jekyll page links
                        def replace_link(match):
                            path = match.group(1)
                            
                            # Determine the relative path based on file location
                            rel_path = os.path.relpath(filepath, vault_dir).replace('\\', '/')
                            
                            # Count directory levels to build correct relative path
                            levels = rel_path.count('/')
                            
                            if levels == 1:  # In a top-level directory
                                if path.startswith('02_Concepts/'):
                                    return f"../{path.replace('.md', '/')}".replace('02_Concepts/', '02_Concepts/')
                                elif path.startswith('01_Course/'):
                                    return f"../{path.replace('.md', '/')}".replace('01_Course/', '01_Course/')
                                else:
                                    return f"../{path.replace('.md', '/')}".replace('.md', '/')
                            elif levels == 2:  # In a subdirectory
                                if path.startswith('02_Concepts/'):
                                    return f"../../{path.replace('.md', '/')}".replace('02_Concepts/', '02_Concepts/')
                                elif path.startswith('01_Course/'):
                                    return f"../../{path.replace('.md', '/')}".replace('01_Course/', '01_Course/')
                                else:
                                    return f"../../{path.replace('.md', '/')}".replace('.md', '/')
                            else:
                                return f"../{path.replace('.md', '/')}".replace('.md', '/')
                        
                        # Replace all GitHub links
                        new_content = re.sub(github_pattern, replace_link, content)
                        
                        if new_content != content:
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            count += 1
                            print(f"Fixed links in: {filepath}")
                
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")
    
    print(f"Fixed GitHub links in {count} HTML files")

if __name__ == "__main__":
    fix_github_links_in_html()