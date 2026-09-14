<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="UTF-8"/>
  <xsl:template match="/catalog">
    <html>
      <body>
        <h1>Catalog</h1>
        <ul>
          <xsl:for-each select="product">
            <li>
              <xsl:value-of select="@name"/>
              <xsl:text> — $</xsl:text>
              <xsl:value-of select="price"/>
            </li>
          </xsl:for-each>
        </ul>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
