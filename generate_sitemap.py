import os
import datetime

# Configuration
domain = "https://www.hsoneglobal.com"
root_dir = r"H:\accio\HSONE_Premium_B2B_Website_V3_Contact"
exclude_dirs = {'.git', 'assets', 'resources', 'temp_new_site'}

def generate_sitemap():
    links = []
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # Add homepage
    links.append(f"  <url>\n    <loc>{domain}/</loc>\n    <lastmod>{now}</lastmod>\n    <priority>1.0</priority>\n  </url>")

    # Walk through directories
    for root, dirs, files in os.walk(root_dir):
        # Skip excluded dirs
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file == "index.html":
                # Get relative path
                rel_path = os.path.relpath(root, root_dir)
                if rel_path == ".":
                    continue # already added homepage
                
                # Format URL
                url_path = rel_path.replace(os.sep, '/')
                full_url = f"{domain}/{url_path}/"
                
                # Determine priority based on path
                priority = "0.8"
                if "products" in url_path:
                    priority = "0.9"
                
                links.append(f"  <url>\n    <loc>{full_url}</loc>\n    <lastmod>{now}</lastmod>\n    <priority>{priority}</priority>\n  </url>")

    # Build XML
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml_content += "\n".join(links)
    xml_content += '\n</urlset>'
    
    return xml_content

sitemap_xml = generate_sitemap()
with open(os.path.join(root_dir, "sitemap.xml"), 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)

print("sitemap.xml generated with all product links.")
