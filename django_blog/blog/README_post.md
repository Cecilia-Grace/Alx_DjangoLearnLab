Django Blog Post CRUD System

This Django module provides full Create, Read, Update, Delete (CRUD) functionality for blog posts with user authentication and access control.

🚀 Features

List all blog posts

View individual post details

Create new posts (authenticated users only)

Edit and delete posts (only by the author)

CSRF-protected forms

User-friendly templates for all operations

URL Paths
Path	Purpose
/posts/	List all posts
/posts/new/	Create a new post
/posts/<int:pk>/	View post details
/posts/<int:pk>/edit/	Edit a post (author only)
/posts/<int:pk>/delete/	Delete a post (author only)
Usage

Visit /posts/ to see all posts.

Click a post title to view details.

Authenticated users can create new posts at /posts/new/.

Authors can edit or delete their posts from the post detail page.

Permissions & Security

Only logged-in users can create posts.

Only the author can edit or delete a post.

List and detail views are public.

All forms include CSRF protection.