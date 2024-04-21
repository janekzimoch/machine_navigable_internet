import re


text = """

[1] <HTML lang="en"> 
        [2] <BODY data-container="body" id="html-body" class="adminhtml-dashboard-index page-layout-admin-1column"> 
                [3] <DIV class="menu-wrapper _fixed"> 
                        [5] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/" data-edition="Community Edition" class="logo"> 
                                [6] <IMG class="logo-img" src="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/static/version1681922233/adminhtml/Magento/backend/en_US/images/magento-icon.svg" alt="Magento Admin Panel" title="Magento Admin Panel"> 
                        [7] <NAV class="admin__menu"> 
                                [8] <UL id="nav" role="menubar"> 
                                        [9] <LI data-ui-id="menu-magento-backend-dashboard" class="item-dashboard _current _active level-0" id="menu-magento-backend-dashboard" aria-haspopup="true" role="menu-item"> 
                                                [10] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/dashboard/" class="_active"> 
                                                        [13] <#text> Dashboard
                                        [14] <LI data-ui-id="menu-magento-sales-sales" class="item-sales parent level-0" id="menu-magento-sales-sales" aria-haspopup="true" role="menu-item"> 
                                                [15] <A href="#" onclick="return false;" class="focusable-end"> 
                                                        [18] <#text> Sales
                                                [19] <DIV class="submenu" aria-labelledby="menu-magento-sales-sales"> 
                                                        [20] <STRONG class="submenu-title"> 
                                                        [21] <A href="#" class="action-close _close" data-role="close-submenu"> 
                                                        [23] <UL role="menu"> 
                                                                [24] <LI data-ui-id="menu-magento-sales-sales-operation" class="item-sales-operation parent level-1" role="menu-item"> 
                                                                        [25] <DIV class="submenu"> 
                                                                                [26] <UL role="menu"> 
                                                                                        [27] <LI data-ui-id="menu-magento-sales-sales-order" class="item-sales-order level-2" role="menu-item"> 
                                                                                                [28] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/sales/order/" class="focusable-end"> 
                                                                                        [29] <LI data-ui-id="menu-magento-sales-sales-invoice" class="item-sales-invoice level-2" role="menu-item"> 
                                                                                                [30] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/sales/invoice/" class="focusable-end"> 
                                                                                        [31] <LI data-ui-id="menu-magento-sales-sales-shipment" class="item-sales-shipment level-2" role="menu-item"> 
                                                                                                [32] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/sales/shipment/" class="focusable-end"> 
                                                                                        [33] <LI data-ui-id="menu-magento-sales-sales-creditmemo" class="item-sales-creditmemo level-2" role="menu-item"> 
                                                                                                [34] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/sales/creditmemo/" class="focusable-end"> 
                                                                                        [35] <LI data-ui-id="menu-magento-paypal-paypal-billing-agreement" class="item-paypal-billing-agreement level-2" role="menu-item"> 
                                                                                                [36] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/paypal/billing_agreement/" class="focusable-end"> 
                                                                                        [37] <LI data-ui-id="menu-magento-sales-sales-transactions" class="item-sales-transactions level-2" role="menu-item"> 
                                                                                                [38] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/sales/transactions/" class="focusable-end"> 
                                                                                        [39] <LI data-ui-id="menu-paypal-braintree-virtual-terminal" class="item-virtual-terminal level-2" role="menu-item"> 
                                                                                                [40] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/braintree/virtual/" class="focusable-end"> 
                                                                                                        [42] <#text> Braintree Virtual Terminal
                                        [43] <LI data-ui-id="menu-magento-catalog-catalog" class="item-catalog parent level-0" id="menu-magento-catalog-catalog" aria-haspopup="true" role="menu-item"> 
                                                [44] <A href="#" onclick="return false;" class="focusable-end"> 
                                                        [47] <#text> Catalog
                                                [48] <DIV class="submenu" aria-labelledby="menu-magento-catalog-catalog"> 
                                                        [49] <STRONG class="submenu-title"> 
                                                        [50] <A href="#" class="action-close _close" data-role="close-submenu"> 
                                                        [52] <UL role="menu"> 
                                                                [53] <LI data-ui-id="menu-magento-catalog-inventory" class="item-inventory parent level-1" role="menu-item"> 
                                                                        [54] <DIV class="submenu"> 
                                                                                [55] <UL role="menu"> 
                                                                                        [56] <LI data-ui-id="menu-magento-catalog-catalog-products" class="item-catalog-products level-2" role="menu-item"> 
                                                                                                [57] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/catalog/product/" class="focusable-end"> 
                                                                                        [58] <LI data-ui-id="menu-magento-catalog-catalog-categories" class="item-catalog-categories level-2" role="menu-item"> 
                                                                                                [59] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/catalog/category/" class="focusable-end"> 
                                        [60] <LI data-ui-id="menu-magento-customer-customer" class="item-customer parent level-0" id="menu-magento-customer-customer" aria-haspopup="true" role="menu-item"> 
                                                [61] <A href="#" onclick="return false;" class="focusable-end"> 
                                                        [64] <#text> Customers
                                                [65] <DIV class="submenu" aria-labelledby="menu-magento-customer-customer"> 
                                                        [66] <STRONG class="submenu-title"> 
                                                        [67] <A href="#" class="action-close _close" data-role="close-submenu"> 
                                                        [69] <UL role="menu"> 
                                                                [70] <LI data-ui-id="menu-magento-customer-customer-manage" class="item-customer-manage level-1" role="menu-item"> 
                                                                        [71] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/customer/index/" class="focusable-end"> 
                                                                [72] <LI data-ui-id="menu-magento-customer-customer-online" class="item-customer-online level-1" role="menu-item"> 
                                                                        [73] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/customer/online/" class="focusable-end"> 
                                                                [74] <LI data-ui-id="menu-magento-loginascustomerlog-login-log" class="item-login-log level-1" role="menu-item"> 
                                                                        [75] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/loginascustomer_log/log/index/" class="focusable-end"> 
                                                                [76] <LI data-ui-id="menu-magento-customer-customer-group" class="item-customer-group level-1" role="menu-item"> 
                                                                        [77] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/customer/group/" class="focusable-end"> 
                                        [78] <LI data-ui-id="menu-magento-backend-marketing" class="item-marketing parent level-0" id="menu-magento-backend-marketing" aria-haspopup="true" role="menu-item"> 
                                                [79] <A href="#" onclick="return false;" class="focusable-end"> 
                                                        [82] <#text> Marketing
                                                [83] <DIV class="submenu" aria-labelledby="menu-magento-backend-marketing"> 
                                                        [84] <STRONG class="submenu-title"> 
                                                        [85] <A href="#" class="action-close _close" data-role="close-submenu"> 
                                                        [87] <UL role="menu"> 
                                                                [88] <LI class="column"> 
                                                                        [89] <UL role="menu"> 
                                                                                [90] <LI data-ui-id="menu-magento-backend-marketing-seo" class="item-marketing-seo parent level-1" role="menu-item"> 
                                                                                        [91] <STRONG class="submenu-group-title" role="presentation"> 
                                                                                        [92] <DIV class="submenu"> 
                                                                                                [93] <UL role="menu"> 
                                                                                                        [94] <LI data-ui-id="menu-magento-urlrewrite-urlrewrite" class="item-urlrewrite level-2" role="menu-item"> 
                                                                                                                [95] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/url_rewrite/index/" class="focusable-end"> 
                                                                                                        [96] <LI data-ui-id="menu-magento-search-search-terms" class="item-search-terms level-2" role="menu-item"> 
                                                                                                                [97] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/search/term/index/" class="focusable-end"> 
                                                                                                        [98] <LI data-ui-id="menu-magento-search-search-synonyms" class="item-search-synonyms level-2" role="menu-item"> 
                                                                                                                [99] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/search/synonyms/index/" class="focusable-end"> 
                                                                                                        [100] <LI data-ui-id="menu-magento-sitemap-catalog-sitemap" class="item-catalog-sitemap level-2" role="menu-item"> 
                                                                                                                [101] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/sitemap/" class="focusable-end"> 
                                                                                [102] <LI data-ui-id="menu-magento-backend-marketing-user-content" class="item-marketing-user-content parent level-1" role="menu-item"> 
                                                                                        [103] <STRONG class="submenu-group-title" role="presentation"> 
                                                                                        [104] <DIV class="submenu"> 
                                                                                                [105] <UL role="menu"> 
                                                                                                        [106] <LI data-ui-id="menu-magento-review-catalog-reviews-ratings-reviews-all" class="item-catalog-reviews-ratings-reviews-all level-2" role="menu-item"> 
                                                                                                                [107] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/review/product/index/" class="focusable-end"> 
                                                                                                        [108] <LI data-ui-id="menu-magento-review-catalog-reviews-ratings-pending" class="item-catalog-reviews-ratings-pending level-2" role="menu-item"> 
                                                                                                                [109] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/review/product/pending/" class="focusable-end"> 
                                        [110] <LI data-ui-id="menu-magento-backend-content" class="item-content parent level-0" id="menu-magento-backend-content" aria-haspopup="true" role="menu-item"> 
                                                [111] <A href="#" onclick="return false;" class="focusable-end"> 
                                                        [114] <#text> Content
                                                [115] <DIV class="submenu" aria-labelledby="menu-magento-backend-content"> 
                                                        [116] <STRONG class="submenu-title"> 
                                                        [117] <A href="#" class="action-close _close" data-role="close-submenu"> 
                                                        [119] <UL role="menu"> 
                                                                [120] <LI data-ui-id="menu-magento-backend-content-elements" class="item-content-elements parent level-1" role="menu-item"> 
                                                                        [121] <STRONG class="submenu-group-title" role="presentation"> 
                                                                        [122] <DIV class="submenu"> 
                                                                                [123] <UL role="menu"> 
                                                                                        [124] <LI data-ui-id="menu-magento-cms-cms-page" class="item-cms-page level-2" role="menu-item"> 
                                                                                                [125] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/cms/page/" class="focusable-end"> 
                                                                                        [126] <LI data-ui-id="menu-magento-cms-cms-block" class="item-cms-block level-2" role="menu-item"> 
                                                                                                [127] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/cms/block/" class="focusable-end"> 
                                                                                        [128] <LI data-ui-id="menu-magento-widget-cms-widget-instance" class="item-cms-widget-instance level-2" role="menu-item"> 
                                                                                                [129] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/widget_instance/" class="focusable-end"> 
                                                                                        [130] <LI data-ui-id="menu-magento-pagebuilder-templates" class="item-templates level-2" role="menu-item"> 
                                                                                                [131] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/pagebuilder/template/" class="focusable-end"> 
                                                                [132] <LI data-ui-id="menu-magento-mediagalleryui-media" class="item-media parent level-1" role="menu-item"> 
                                                                        [133] <STRONG class="submenu-group-title" role="presentation"> 
                                                                        [134] <DIV class="submenu"> 
                                                                                [135] <UL role="menu"> 
                                                                                        [136] <LI data-ui-id="menu-magento-mediagalleryui-media-gallery" class="item-media-gallery level-2" role="menu-item"> 
                                                                                                [137] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/media_gallery/media/index/" class="focusable-end"> 
                                                                [138] <LI data-ui-id="menu-magento-backend-system-design" class="item-system-design parent level-1" role="menu-item"> 
                                                                        [139] <STRONG class="submenu-group-title" role="presentation"> 
                                                                        [140] <DIV class="submenu"> 
                                                                                [141] <UL role="menu"> 
                                                                                        [142] <LI data-ui-id="menu-magento-theme-design-config" class="item-design-config level-2" role="menu-item"> 
                                                                                                [143] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/theme/design_config/" class="focusable-end"> 
                                                                                        [144] <LI data-ui-id="menu-magento-theme-system-design-theme" class="item-system-design-theme level-2" role="menu-item"> 
                                                                                                [145] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/system_design_theme/" class="focusable-end"> 
                                                                                        [146] <LI data-ui-id="menu-magento-backend-system-design-schedule" class="item-system-design-schedule level-2" role="menu-item"> 
                                                                                                [147] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/system_design/" class="focusable-end"> 
                                        [148] <LI data-ui-id="menu-magento-reports-report" class="item-report parent level-0" id="menu-magento-reports-report" aria-haspopup="true" role="menu-item"> 
                                                [149] <A href="#" onclick="return false;" class="focusable-end"> 
                                                        [152] <#text> Reports
                                                [153] <DIV class="submenu" aria-labelledby="menu-magento-reports-report"> 
                                                        [154] <STRONG class="submenu-title"> 
                                                        [155] <A href="#" class="action-close _close" data-role="close-submenu"> 
                                                        [157] <UL role="menu"> 
                                                                [158] <LI class="column"> 
                                                                        [159] <UL role="menu"> 
                                                                                [160] <LI data-ui-id="menu-magento-analytics-business-intelligence" class="item-business-intelligence parent level-1" role="menu-item"> 
                                                                                        [161] <STRONG class="submenu-group-title" role="presentation"> 
                                                                                                [163] <#text> Business Intelligence
                                                                                        [164] <DIV class="submenu"> 
                                                                                                [165] <UL role="menu"> 
                                                                                                        [166] <LI data-ui-id="menu-magento-analytics-advanced-reporting" class="item-advanced-reporting level-2" role="menu-item"> 
                                                                                                                [167] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/analytics/reports/show/" target="_blank" class="focusable-end"> 
                                                                                                        [168] <LI data-ui-id="menu-magento-analytics-bi-essentials" class="item-bi-essentials level-2" role="menu-item"> 
                                                                                                                [169] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/analytics/biessentials/signup/" target="_blank" class="focusable-end"> 
                                        [170] <LI data-ui-id="menu-magento-backend-stores" class="item-stores parent level-0" id="menu-magento-backend-stores" aria-haspopup="true" role="menu-item"> 
                                                [171] <A href="#" onclick="return false;" class="focusable-end"> 
                                                        [174] <#text> Stores
                                                [175] <DIV class="submenu" aria-labelledby="menu-magento-backend-stores"> 
                                                        [176] <STRONG class="submenu-title"> 
                                                        [177] <A href="#" class="action-close _close" data-role="close-submenu"> 
                                                        [179] <UL role="menu"> 
                                                                [180] <LI class="column"> 
                                                                        [181] <UL role="menu"> 
                                                                                [182] <LI data-ui-id="menu-magento-currencysymbol-system-currency" class="item-system-currency parent level-1" role="menu-item"> 
                                                                                        [183] <STRONG class="submenu-group-title" role="presentation"> 
                                                                                        [184] <DIV class="submenu"> 
                                                                                                [185] <UL role="menu"> 
                                                                                                        [186] <LI data-ui-id="menu-magento-currencysymbol-system-currency-rates" class="item-system-currency-rates level-2" role="menu-item"> 
                                                                                                                [187] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/system_currency/" class="focusable-end"> 
                                                                                                        [188] <LI data-ui-id="menu-magento-currencysymbol-system-currency-symbols" class="item-system-currency-symbols level-2" role="menu-item"> 
                                                                                                                [189] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/system_currencysymbol/" class="focusable-end"> 
                                                                                [190] <LI data-ui-id="menu-magento-backend-stores-attributes" class="item-stores-attributes parent level-1" role="menu-item"> 
                                                                                        [191] <STRONG class="submenu-group-title" role="presentation"> 
                                                                                        [192] <DIV class="submenu"> 
                                                                                                [193] <UL role="menu"> 
                                                                                                        [194] <LI data-ui-id="menu-magento-catalog-catalog-attributes-attributes" class="item-catalog-attributes-attributes level-2" role="menu-item"> 
                                                                                                                [195] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/catalog/product_attribute/" class="focusable-end"> 
                                                                                                        [196] <LI data-ui-id="menu-magento-catalog-catalog-attributes-sets" class="item-catalog-attributes-sets level-2" role="menu-item"> 
                                                                                                                [197] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/catalog/product_set/" class="focusable-end"> 
                                                                                                        [198] <LI data-ui-id="menu-magento-review-catalog-reviews-ratings-ratings" class="item-catalog-reviews-ratings-ratings level-2" role="menu-item"> 
                                                                                                                [199] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/review/rating/" class="focusable-end"> 
                                        [200] <LI data-ui-id="menu-magento-backend-system" class="item-system parent level-0" id="menu-magento-backend-system" aria-haspopup="true" role="menu-item"> 
                                                [201] <A href="#" onclick="return false;" class="focusable-end"> 
                                                        [204] <#text> System
                                                [205] <DIV class="submenu" aria-labelledby="menu-magento-backend-system"> 
                                                        [206] <STRONG class="submenu-title"> 
                                                        [207] <A href="#" class="action-close _close" data-role="close-submenu"> 
                                                        [209] <UL role="menu"> 
                                                                [210] <LI class="column"> 
                                                                        [211] <UL role="menu"> 
                                                                                [212] <LI data-ui-id="menu-magento-user-system-acl" class="item-system-acl parent level-1" role="menu-item"> 
                                                                                        [213] <STRONG class="submenu-group-title" role="presentation"> 
                                                                                        [214] <DIV class="submenu"> 
                                                                                                [215] <UL role="menu"> 
                                                                                                        [216] <LI data-ui-id="menu-magento-user-system-acl-users" class="item-system-acl-users level-2" role="menu-item"> 
                                                                                                                [217] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/user/" class="focusable-end"> 
                                                                                                        [218] <LI data-ui-id="menu-magento-user-system-acl-locks" class="item-system-acl-locks level-2" role="menu-item"> 
                                                                                                                [219] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/locks/" class="focusable-end"> 
                                                                                                        [220] <LI data-ui-id="menu-magento-user-system-acl-roles" class="item-system-acl-roles level-2" role="menu-item"> 
                                                                                                                [221] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/user_role/" class="focusable-end"> 
                                                                                [222] <LI data-ui-id="menu-magento-asynchronousoperations-system-magento-logging" class="item-system-magento-logging parent level-1" role="menu-item"> 
                                                                                        [223] <STRONG class="submenu-group-title" role="presentation"> 
                                                                                        [224] <DIV class="submenu"> 
                                                                                                [225] <UL role="menu"> 
                                                                                                        [226] <LI data-ui-id="menu-magento-asynchronousoperations-system-magento-logging-bulk-operations" class="item-system-magento-logging-bulk-operations level-2" role="menu-item"> 
                                                                                                                [227] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/bulk/index/" class="focusable-end"> 
                                                                                [228] <LI data-ui-id="menu-magento-backend-system-other-settings" class="item-system-other-settings parent level-1" role="menu-item"> 
                                                                                        [229] <STRONG class="submenu-group-title" role="presentation"> 
                                                                                        [230] <DIV class="submenu"> 
                                                                                                [231] <UL role="menu"> 
                                                                                                        [232] <LI data-ui-id="menu-magento-adminnotification-system-adminnotification" class="item-system-adminnotification level-2" role="menu-item"> 
                                                                                                                [233] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/notification/" class="focusable-end"> 
                                                                                                        [234] <LI data-ui-id="menu-magento-variable-system-variable" class="item-system-variable level-2" role="menu-item"> 
                                                                                                                [235] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/system_variable/" class="focusable-end"> 
                                                                                                        [236] <LI data-ui-id="menu-magento-encryptionkey-system-crypt-key" class="item-system-crypt-key level-2" role="menu-item"> 
                                                                                                                [237] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/crypt_key/" class="focusable-end"> 
                                                                                                                        [239] <#text> Manage Encryption Key
                                        [240] <LI data-ui-id="menu-magento-marketplace-partners" class="item-partners last level-0" id="menu-magento-marketplace-partners" aria-haspopup="true" role="menu-item"> 
                                                [241] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/marketplace/index/" class="focusable-end"> 
                                                        [245] <#text> Find Partners & Extensions
                [246] <DIV class="page-wrapper"> 
                        [247] <DIV class="notices-wrapper"> 
                                [248] <DIV class="admin__data-grid-outer-wrap" data-bind="scope: 'notification_area.notification_area'"> 
                                        [249] <DIV id="system_messages" class="message-system" data-bind="visible: totalRecords, collapsible"> 
                                                [250] <DIV class="message-system-inner" data-bind="outerClick: fixLoaderHeight.bind($data, true)"> 
                                                        [251] <DIV class="message-system-short"> 
                                                                [252] <BUTTON class="message-system-action-dropdown" data-bind="toggleCollapsible"> 
                                                                        [256] <#text> System Messages
                                                                        [257] <#text> :
                                                                        [258] <#text> 1
                                                                [259] <DIV class="message-system-short-wrapper" data-bind="visible: !$collapsible.opened()" data-repeat-index="0"> 
                                                                        [260] <DIV data-bind="css: $col.getFieldClass($row()), html: $col.getLabelUnsanitizedHtml($row())" class="message message-warning"> 
                                                                                [262] <#text> Failed to synchronize data to the Magento Business Intelligence service.
                                                                                [263] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/analytics/subscription/retry/"> 
                                                                                        [264] <#text> Retry Synchronization
                        [265] <HEADER class="page-header row"> 
                                [266] <DIV class="page-header-hgroup col-l-8 col-m-6"> 
                                        [267] <DIV class="page-title-wrapper"> 
                                                [268] <H1 class="page-title"> 
                                                        [269] <#text> Dashboard
                                [270] <DIV class="page-header-actions col-l-4 col-m-6"> 
                                        [271] <DIV class="admin-user admin__action-dropdown-wrap"> 
                                                [272] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/system_account/index/" class="admin__action-dropdown" title="My Account" data-toggle="dropdown"> 
                                                        [275] <SPAN class="admin__action-dropdown-text"> 
                                                                [276] <SPAN class="admin-user-account-text"> 
                                                                        [277] <#text> admin
                                        [278] <DIV class="notifications-wrapper admin__action-dropdown-wrap" data-notification-count="0"> 
                                                [279] <A class="notifications-action admin__action-dropdown" href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/notification/index/" title="Notifications"> 
                                        [281] <LABEL class="search-global-label" for="search-global"> 
                                        [283] <INPUT type="text" class="search-global-input" id="search-global" autocomplete="off" style="focusable-end"> 
                        [284] <MAIN id="anchor-content" class="page-content"> 
                                [285] <DIV class="page-main-actions"> 
                                        [286] <DIV class="store-switcher store-view"> 
                                                [287] <SPAN class="store-switcher-label"> 
                                                        [288] <#text> Scope:
                                                [290] <DIV class="actions dropdown closable"> 
                                                        [291] <BUTTON type="button" class="admin__action-dropdown" data-toggle="dropdown" aria-haspopup="true" id="store-change-button"> 
                                                                [293] <#text> All Store Views
                                                [295] <A href="https://docs.magento.com/user-guide/configuration/scope.html" onclick="this.target='_blank'" title="What is this?" class="admin__field-tooltip-action action-help"> 
                                                        [298] <#text> What is this?
                                        [299] <DIV class="page-actions-buttons"> 
                                                [300] <FORM class="action-element" action="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/dashboard/refreshStatistics/" method="post"> 
                                                        [301] <BUTTON class="action-primary" type="submit" title="Reload Data"> 
                                                                [302] <#text> Reload Data
                                [303] <DIV id="page:main-container" class="page-columns"> 
                                        [304] <DIV class="admin__old"> 
                                                [305] <DIV id="container" class="main-col"> 
                                                        [306] <SECTION class="dashboard-advanced-reports" data-index="dashboard-advanced-reports"> 
                                                                [307] <DIV class="dashboard-advanced-reports-description"> 
                                                                        [308] <HEADER class="dashboard-advanced-reports-title"> 
                                                                                [309] <#text> Advanced Reporting
                                                                        [310] <DIV class="dashboard-advanced-reports-content"> 
                                                                                [311] <#text> Gain new insights and take command of your business' performance, using our dynamic product, order, and customer reports tailored to your customer data.
                                                                [312] <DIV class="dashboard-advanced-reports-actions"> 
                                                                        [313] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/analytics/reports/show/" target="_blank" class="action action-advanced-reports" data-index="analytics-service-link" title="Go to Advanced Reporting"> 
                                                                                [316] <#text> Go to Advanced Reporting
                                                        [318] <DIV class="dashboard-container row"> 
                                                                [319] <DIV class="dashboard-main col-m-8 col-m-push-4"> 
                                                                        [320] <DIV class="dashboard-diagram-container"> 
                                                                                [321] <DIV class="dashboard-diagram-disabled"> 
                                                                                        [322] <#text> Chart is disabled. To enable the chart, click
                                                                                        [323] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/system_config/edit/section/admin/#admin_dashboard-link"> 
                                                                                                [324] <#text> here
                                                                                        [325] <#text> .
                                                                        [326] <DIV class="dashboard-totals" id="dashboard_diagram_totals"> 
                                                                                [327] <UL class="dashboard-totals-list"> 
                                                                                        [328] <LI class="dashboard-totals-item"> 
                                                                                                [329] <SPAN class="dashboard-totals-label"> 
                                                                                                        [330] <#text> Revenue
                                                                                                [331] <STRONG class="dashboard-totals-value"> 
                                                                                                        [332] <SPAN class="price"> 
                                                                                                                [333] <#text> $0.00
                                                                                        [334] <LI class="dashboard-totals-item"> 
                                                                                                [335] <SPAN class="dashboard-totals-label"> 
                                                                                                        [336] <#text> Tax
                                                                                                [337] <STRONG class="dashboard-totals-value"> 
                                                                                                        [338] <SPAN class="price"> 
                                                                                                                [339] <#text> $0.00
                                                                                        [340] <LI class="dashboard-totals-item"> 
                                                                                                [341] <SPAN class="dashboard-totals-label"> 
                                                                                                        [342] <#text> Shipping
                                                                                                [343] <STRONG class="dashboard-totals-value"> 
                                                                                                        [344] <SPAN class="price"> 
                                                                                                                [345] <#text> $0.00
                                                                                        [346] <LI class="dashboard-totals-item"> 
                                                                                                [347] <SPAN class="dashboard-totals-label"> 
                                                                                                        [348] <#text> Quantity
                                                                                                [349] <STRONG class="dashboard-totals-value"> 
                                                                                                        [350] <#text> 0
                                                                        [351] <DIV class="dashboard-store-stats"> 
                                                                                [352] <DIV id="grid_tab" class="ui-tabs ui-corner-all ui-widget ui-widget-content"> 
                                                                                        [354] <UL class="tabs-horiz ui-tabs-nav ui-helper-reset ui-helper-clearfix ui-widget-header ui-corner-all" role="tablist"> 
                                                                                                [355] <LI class="ui-state-default ui-corner-top ui-tabs-active ui-state-active" role="tab" tabindex="0" aria-controls="grid_tab_ordered_products_content" aria-labelledby="grid_tab_ordered_products" aria-selected="true" aria-expanded="true"> 
                                                                                                        [356] <A href="#grid_tab_ordered_products_content" id="grid_tab_ordered_products" title="Bestsellers" class="tab-item-link ui-tabs-anchor" data-tab-type="focusable-end" role="presentation" tabindex="-1"> 
                                                                                                                [358] <#text> Bestsellers
                                                                                                [360] <LI class="ui-state-default ui-corner-top" role="tab" tabindex="-1" aria-controls="ui-id-1" aria-labelledby="grid_tab_reviewed_products" aria-selected="false" aria-expanded="false"> 
                                                                                                        [361] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/dashboard/productsViewed/" id="grid_tab_reviewed_products" title="Most Viewed Products" class="tab-item-link ajax notloaded ui-tabs-anchor" data-tab-type="focusable-end" role="presentation" tabindex="-1"> 
                                                                                                                [363] <#text> Most Viewed Products
                                                                                                [365] <LI class="ui-state-default ui-corner-top" role="tab" tabindex="-1" aria-controls="ui-id-2" aria-labelledby="grid_tab_new_customers" aria-selected="false" aria-expanded="false"> 
                                                                                                        [366] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/dashboard/customersNewest/" id="grid_tab_new_customers" title="New Customers" class="tab-item-link ajax notloaded ui-tabs-anchor" data-tab-type="focusable-end" role="presentation" tabindex="-1"> 
                                                                                                                [368] <#text> New Customers
                                                                                                [370] <LI class="ui-state-default ui-corner-top" role="tab" tabindex="-1" aria-controls="ui-id-3" aria-labelledby="grid_tab_customers" aria-selected="false" aria-expanded="false"> 
                                                                                                        [371] <A href="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/admin/dashboard/customersMost/" id="grid_tab_customers" title="Customers" class="tab-item-link ajax notloaded ui-tabs-anchor" data-tab-type="focusable-end" role="presentation" tabindex="-1"> 
                                                                                                                [373] <#text> Customers
                                                                                [374] <DIV id="grid_tab_content" class="dashboard-store-stats-content"> 
                                                                                        [375] <DIV id="grid_tab_ordered_products_content" aria-labelledby="grid_tab_ordered_products" class="ui-tabs-panel ui-widget-content ui-corner-bottom" role="tabpanel" aria-hidden="false" style="focusable-end"> 
                                                                                                [376] <DIV class="dashboard-item-content"> 
                                                                                                        [377] <TABLE class="admin__table-primary dashboard-data" id="productsOrderedGrid_table"> 
                                                                                                                [380] <TH class="data-grid-th col-product no-link col-name"> 
                                                                                                                        [382] <#text> Product
                                                                                                                [383] <TH class="data-grid-th no-link col-price"> 
                                                                                                                        [385] <#text> Price
                                                                                                                [386] <TH class="data-grid-th col-qty no-link col-ordered_qty"> 
                                                                                                                        [388] <#text> Quantity
                                                                                                                [390] <TR title="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/catalog/product/edit/id/20/" class="even"> 
                                                                                                                        [391] <TD class="col-product col-name"> 
                                                                                                                                [392] <#text> Quest Lumaflex™ Band
                                                                                                                        [393] <TD class="col-price a-right"> 
                                                                                                                                [394] <#text> $19.00
                                                                                                                        [395] <TD class="col-qty col-ordered_qty col-number last"> 
                                                                                                                                [396] <#text> 6
                                                                [397] <DIV class="dashboard-secondary col-m-4 col-m-pull-8"> 
                                                                        [398] <DIV class="dashboard-item dashboard-item-primary"> 
                                                                                [399] <DIV class="dashboard-item-title"> 
                                                                                        [400] <#text> Lifetime Sales
                                                                                [401] <DIV class="dashboard-item-content"> 
                                                                                        [402] <STRONG class="dashboard-sales-value"> 
                                                                                                [403] <SPAN class="price"> 
                                                                                                        [404] <#text> $0.00
                                                                        [405] <DIV class="dashboard-item dashboard-item-primary"> 
                                                                                [406] <DIV class="dashboard-item-title"> 
                                                                                        [407] <#text> Average Order
                                                                                [408] <DIV class="dashboard-item-content"> 
                                                                                        [409] <STRONG class="dashboard-sales-value"> 
                                                                                                [410] <SPAN class="price"> 
                                                                                                        [411] <#text> $0.00
                                                                        [412] <DIV class="dashboard-item"> 
                                                                                [413] <DIV class="dashboard-item-title"> 
                                                                                        [414] <#text> Last Orders
                                                                                [415] <DIV class="dashboard-item-content"> 
                                                                                        [416] <TABLE class="admin__table-primary dashboard-data" id="lastOrdersGrid_table"> 
                                                                                                [419] <TH class="data-grid-th no-link col-customer"> 
                                                                                                        [421] <#text> Customer
                                                                                                [422] <TH class="data-grid-th no-link col-items"> 
                                                                                                        [424] <#text> Items
                                                                                                [425] <TH class="data-grid-th no-link col-total"> 
                                                                                                        [427] <#text> Total
                                                                                                [429] <TR title="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/sales/order/view/order_id/299/" class="even"> 
                                                                                                        [430] <TD class="col-customer"> 
                                                                                                                [431] <#text> Sarah Miller
                                                                                                        [432] <TD class="col-items col-number"> 
                                                                                                                [433] <#text> 5
                                                                                                        [434] <TD class="col-total a-right last"> 
                                                                                                                [435] <#text> $194.40
                                                                                                [436] <TR title="http://ec2-3-22-150-63.us-east-2.compute.amazonaws.com:7780/admin/sales/order/view/order_id/65/"> 
                                                                                                        [437] <TD class="col-customer"> 
                                                                                                                [438] <#text> Grace Nguyen
                                                                                                        [439] <TD class="col-items col-number"> 
                                                                                                                [440] <#text> 4
                                                                                                        [441] <TD class="col-total a-right last"> 
                                                                                                                [442] <#text> $190.00
                [443] <ASIDE role="dialog" class="modal-slide notification_area_notification_area_modalContainer_modal" aria-describedby="modal-content-9" data-role="modal" data-type="slide" tabindex="0"> 

"""

def extract_html_info(line: str):
# Regex to extract the id, tag, and attributes
    pattern = re.compile(r'\[(\d+)\]\s*<(\w+)(.*?)>')
    
    # Find matches in the given line
    match = pattern.search(line)
    if not match:
        return None

    id = match.group(1)
    tag = match.group(2)
    attributes_string = match.group(3).strip()

    # Extract attributes into a dictionary
    attrs_pattern = re.compile(r'(\w+)="([^"]*)"')
    attributes = dict(attrs_pattern.findall(attributes_string))

    return {
        'id': id,
        'tag': tag,
        'dict': attributes
    }




pattern = re.compile(r'\[(\d+)\]\s*<(\w+)(.*?)>')
lines = text.split('\n')
clickable_components = []
for line in lines:
    info = extract_html_info(line)
    if info is None:
        continue
    if info['tag'] in ['A', 'BUTTON'] or 'onclick' in info['dict']:
        clickable_components.append(info)
        print(info)




# for item in clickable_regex.finditer(text):
#     print(item.groups())
#     print(item.group(1))
#     print(item.group(2))
#     print(item.group(3))



