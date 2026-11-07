<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9">
	<xsl:output method="html" encoding="UTF-8" indent="yes"/>
	<xsl:template match="/">
		<html>
			<head>
				<title>XML Sitemap</title>
				<style>
					body { font-family: Arial, Helvetica, sans-serif; font-size: 14px; color: #333; margin: 20px; }
					h1 { font-size: 18px; }
					.count { color: #666; margin-bottom: 10px; }
					table { border-collapse: collapse; width: 100%; }
					th { text-align: left; background: #f2f2f2; padding: 8px; border-bottom: 2px solid #ddd; }
					td { padding: 8px; border-bottom: 1px solid #eee; word-break: break-all; }
					tr:hover { background: #f9f9f9; }
					a { color: #0645ad; text-decoration: none; }
					a:hover { text-decoration: underline; }
				</style>
			</head>
			<body>
				<h1>XML Sitemap</h1>
				<div class="count">
					<xsl:value-of select="count(sitemap:urlset/sitemap:url)"/> URL(s)
				</div>
				<table>
					<tr>
						<th>URL</th>
						<th>Change Frequency</th>
					</tr>
					<xsl:for-each select="sitemap:urlset/sitemap:url">
						<tr>
							<td><a href="{sitemap:loc}"><xsl:value-of select="sitemap:loc"/></a></td>
							<td><xsl:value-of select="sitemap:changefreq"/></td>
						</tr>
					</xsl:for-each>
				</table>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>
