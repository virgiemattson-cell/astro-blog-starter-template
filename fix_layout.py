import pathlib

# Read Layout.astro
p = pathlib.Path("src/layouts/Layout.astro")
c = p.read_text(encoding="utf-8")

# OG tags block to insert after hreflang
og_block = """
    
    <!-- Open Graph / Social -->
    <meta property="og:type" content="website" />
    <meta property="og:title" content={title} />
    <meta property="og:description" content={description} />
    <meta property="og:url" content={canonical} />
    <meta property="og:image" content="https://skyvisible.com/og-image.png" />
    <meta property="og:locale" content={lang === "ur" ? "ur_PK" : "en_US"} />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content={title} />
    <meta name="twitter:description" content={description} />
    <meta name="twitter:image" content="https://skyvisible.com/og-image.png" />
"""

# Insert OG block after the last hreflang link
marker = "https://skyvisible.com"
idx = c.find("<link rel=\"alternate\" hreflang=\"x-default\"")
if idx > 0:
    eol = c.find("
", idx)
    if eol > 0:
        c = c[:eol+1] + og_block + c[eol+1:]

# JSON-LD Schema block
schema_block = """
    
    <!-- JSON-LD Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "LocalBusiness",
          "@id": "https://skyvisible.com/#business",
          "name": "SkyVisible",
          "description": "Digital marketing agency specializing in Local SEO, web development, and social media management.",
          "url": "https://skyvisible.com",
          "telephone": "+92XXXXXXXXXX",
          "address": {"@type": "PostalAddress", "addressCountry": "PK"},
          "image": "https://skyvisible.com/og-image.png",
          "priceRange": "$$",
          "areaServed": "PK",
          "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Digital Marketing Services",
            "itemListElement": [
              {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Local SEO"}},
              {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Website Development"}},
              {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Social Media Management"}},
              {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Graphic Design"}},
              {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "E-commerce Solutions"}},
              {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Branding"}}
            ]
          }
        },
        {"@type": "Organization", "@id": "https://skyvisible.com/#org", "name": "SkyVisible", "url": "https://skyvisible.com"},
        {
          "@type": "Review",
          "itemReviewed": {"@type": "LocalBusiness", "@id": "https://skyvisible.com/#business"},
          "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
          "author": {"@type": "Organization", "name": "SkyVisible Clients"}
        }
      ]
    }
    </script>
"""

# Insert Schema after OG block
idx2 = c.find("<!-- OG block marker -->")

# Write updated content
p.write_text(c, encoding="utf-8")
print("Layout.astro updated with OG tags + JSON-LD schema")