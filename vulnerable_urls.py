# vulnerable_urls.py
vulnerable_urls = [
    (r'/etc/passwd', False),
    (r'/etc/shadow', False),
    (r'/\.git', False),
    (r'/\.htaccess', False),
    (r'/\.htpasswd', False),
    (r'/\.env', False),
    (r'/\.log', False),
    (r'/phpmyadmin', False),
    
    # WordPress
    ("/wp-admin", False),
    ("/wp-login.php", False),
    ("/wp-config.php", False),
    ("/xmlrpc.php", False),
    ("/wp-content/plugins", False),
    ("/wp-content/themes", False),
    ("/wp-includes", False),

    # Joomla
    ("/administrator", False),
    ("/index.php?option=com_user&view=reset&layout=confirm", False),
    ("/index.php?option=com_contenthistory&view=history&list[ordering]=&item_id=75&type_id=1", False),

    # phpMyAdmin
    ("/phpmyadmin", False),
    ("/phpMyAdmin", False),
    ("/pma", False),

    # Common PHP files
    ("/config.php", False),
    ("/db.php", False),
    ("/setup.php", False),
    ("/install.php", False),
    ("/upgrade.php", False),

    # Common Apache/Nginx files
    ("/.htaccess", False),
    ("/.htpasswd", False),
    ("/server-status", False),
    ("/server-info", False),

    # Common exploits
    (r"\.\./", True),  # Directory traversal
    (r"\.\.\\", True),  # Directory traversal (Windows)
    (r"\.\.%00/", True),  # Null byte injection
    (r"\.\.%00\\", True),  # Null byte injection (Windows)
    (r"\.\.%c0%af/", True),  # Encoded directory traversal
    (r"\.\.%c0%af\\", True),  # Encoded directory traversal (Windows)
    (r"\.\.%c1%1c/", True),  # Double encoded directory traversal
    (r"\.\.%c1%1c\\", True),  # Double encoded directory traversal (Windows)
    (r"\.\.%c1%9c/", True),  # Double encoded directory traversal
    (r"\.\.%c1%9c\\", True),  # Double encoded directory

    # New patterns
    (r'/config\.php', True),
    (r'/db\.php', True),
    (r'/install\.php', True),
    (r'/update\.php', True),
    (r'/upgrade\.php', True),
    (r'/phpinfo\.php', True),
    (r'/test\.php', True),
    (r'/info\.php', True),
    (r'/readme\.html', True),
    (r'/CHANGELOG\.txt', True),
    (r'/LICENSE\.txt', True),
    (r'/README\.txt', True),
    (r'/composer\.json', True),
    (r'/composer\.lock', True),
    (r'/nginx\.conf', True),
    (r'/web\.config', True),
    (r'/\.ini', True),
    (r'/\.sql', True),
    (r'/\.bak', True),
    (r'/\.tar\.gz', True),
    (r'/\.zip', True),    

    # SQL Injection patterns
    (r"\b' OR '1'='1\b", True),
    (r"\b'; DROP TABLE users; --\b", True),
    (r"\b' OR 'x'='x\b", True),
    (r"\b' OR username LIKE '%admin%\b", True),
    (r"\b' OR 1=1 --\b", True),
    (r"\b' OR 1=1 /*\b", True),
    (r"\b' OR 1=1; --\b", True),
    (r"\b' OR 1=1#\b", True),
    (r"\b' OR 1=1--\b", True),
    (r"\b' OR 1=1;%00\b", True),
    (r"\b' OR 1=1\\x00\b", True),
    (r"\b' OR 1=1\u0000\b", True),
    (r"\b' OR 'text' > 't\b", True),
    (r"\b' OR 'text' LIKE 't%\b", True),
    (r"\b' OR 'text' = N'text\b", True),
    (r"\b' OR 'something' IS NULL; --\b", True),
    (r"\b' OR 'text' > N'text\b", True),
    (r"\b' OR '9999999' = '9999999\b", True),
    (r"\b' OR '7659'='7659\b", True),
    (r"\b' OR 'text' LIKE N'text%\b", True),
    (r"\b' OR 'zz' > 'a\b", True),
    (r"\b' OR 'zz' > N'a\b", True),
    (r"\b' OR 'a' = 'a\b", True),
    (r"\b' OR 'a' > 'a\b", True),
    (r"\b' OR 'a' > N'a\b", True),
    (r"\b' OR 'a' = N'a\b", True),

    # Directory Traversal patterns
    (r"\b../\b", True),
    (r"\b..\\/\b", True),
    (r"\b..;/\b", True),
    (r"\b..%00/\b", True),
    (r"\b..%00\\/\b", True),
    (r"\b..%c0%af/\b", True),
    (r"\b..%c0%af\\/\b", True),
    (r"\b..%c1%1c/\b", True),
    (r"\b..%c1%1c\\/\b", True),
    (r"\b..%c1%9c/\b", True),
    (r"\b..%c1%9c\\/\b", True),
    (r"\b..%c1%pc/\b", True),
    (r"\b..%c1%pc\\/\b", True),
    (r"\b..%c1%8s/\b", True),
    (r"\b..%c1%8s\\/\b", True),
    (r"\b..%c1%1s/\b", True),
    
    # Other chatgpt recommendations.
    ("/admin", False),
    ("/login", False),
    ("/wp-admin", False),
    ("/wp-login.php", False),
    ("/xmlrpc.php", False),
    ("/administrator", False),
    ("/joomla/administrator", False),
    ("/phpmyadmin", False),
    ("/.htaccess", False),
    ("/.git", False),
    ("/.svn", False),
    ("/.env", False),
    ("/config.php", False),
    ("/wp-config.php", False),
    ("/db.php", False),
    ("/db_backup", False),
    ("/backup.sql", False),
    ("/install.php", False),
    ("/setup.php", False),
    ("/phpinfo.php", False),
    ("/test.php", False),
    ("/.bash_history", False),
    ("/.ssh/id_rsa", False),
    ("/.ssh/id_rsa.pub", False),
    ("/.ssh/authorized_keys", False),
    ("/.ssh/known_hosts", False),
    ("/root", False),
    ("/etc/passwd", False),
    ("/etc/shadow", False),
    ("/var/www/html", False),
    ("/server-status", False),
    ("/.DS_Store", False),
    ("/trace.axd", False),
    ("/elmah.axd", False),
    ("/joomla.xml", False),
    ("/.well-known", False),
    ("/.well-known/security.txt", False),
    ("/server-info", False),
    ("/crossdomain.xml", False),
    ("/clientaccesspolicy.xml", False),
    ("/.htpasswd", False),
    ("/.user.ini", False),
    ("/info.php", False),
    ("/.bashrc", False),
    ("/.bash_profile", False),
    ("/.bash_logout", False),
    ("/php.ini", False),
    ("/web.config", False),
    ("/.well-known/assetlinks.json", False),
    ("/.well-known/apple-app-site-association", False),
    ("/.well-known/apple-developer-merchantid-domain-association", False),
    ("/.well-known/change-password", False),
    ("/.well-known/dnt", False),
    ("/.well-known/dnt-policy.txt", False),
    ("/.well-known/security.txt", False)
]