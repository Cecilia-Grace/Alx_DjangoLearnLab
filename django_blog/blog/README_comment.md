Django Blog – Comment Feature (Brief)
Overview

Users can read comments on blog posts.

Authenticated users can add, edit, and delete their own comments.

Comments are linked to the post and author.

Model

Comment: post (FK), author (FK), content (Text), created_at, updated_at.

Forms

CommentForm handles creation and editing of comments.

Includes validation and a text area for content input.

Views

Add: add_comment (authenticated users only).

Edit: CommentUpdateView (author only).

Delete: CommentDeleteView (author only).

Templates

post_detail.html – shows post content and comments; includes form for adding comments.

comment_form.html – edit comment.

comment_confirm_delete.html – delete confirmation.

URLs

/posts/<post_id>/comments/new/ – add comment

/comments/<pk>/edit/ – edit comment

/comments/<pk>/delete/ – delete comment

Usage

View comments on a post detail page.

Authenticated users can add a comment via the form.

Comment authors can edit or delete their comments.

Security

Only authors can edit/delete their comments.

CSRF protection is enabled.

All users can view comments.