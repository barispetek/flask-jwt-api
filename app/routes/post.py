from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from app.models import Post

post_bp = Blueprint("post", __name__, url_prefix="/api/posts")

@post_bp.route("/", methods=["POST"])
@jwt_required()
def create_post():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({"error": "Title and content required"}), 400

    post = Post(title=title, content=content, user_id=current_user_id)
    db.session.add(post)
    db.session.commit()

    return jsonify({"message": "Post created successfully"}), 201

@post_bp.route("/", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    output = []
    for post in posts:
        output.append({
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "created_at": post.created_at.isoformat(),
            "user_id": post.user_id
        })
    return jsonify({"posts": output}), 200

@post_bp.route("/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify({
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "created_at": post.created_at.isoformat(),
        "user_id": post.user_id
    }), 200

@post_bp.route("/<int:post_id>", methods=["PUT"])
@jwt_required()
def update_post(post_id):
    current_user_id = int(get_jwt_identity())
    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user_id:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    post.title = data.get("title", post.title)
    post.content = data.get("content", post.content)
    db.session.commit()

    return jsonify({"message": "Post updated successfully"}), 200

@post_bp.route("/<int:post_id>", methods=["DELETE"])
@jwt_required()
def delete_post(post_id):
    current_user_id = int(get_jwt_identity())
    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user_id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted successfully"}), 200


