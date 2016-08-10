#include <iostream>
#include <vector>

using std::vector;

struct TreeNode
{ // binary tree node
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr){}
};

void freeTreeNode(TreeNode* node_ptr)
{ // recursively free memory used by pointers of TreeNode
    if (node_ptr->left != nullptr)
    {
        freeTreeNode(node_ptr->left);
    }
    if (node_ptr->right != nullptr)
    {
        freeTreeNode(node_ptr->right);
    }
    delete node_ptr;
}

class Traversal
{
public:
    Traversal() {}
    void preorder(TreeNode* root)
    {
        if(root != nullptr)
        {
            traverse_path.push_back(root->val);
            preorder(root->left);
            preorder(root->right);
        }
    }

    void inorder(TreeNode* root)
    {
        if(root != nullptr)
        {
            inorder(root->left);
            traverse_path.push_back(root->val);
            inorder(root->right);
        }
    }

    void postorder(TreeNode* root)
    {
        if(root != nullptr)
        {
            postorder(root->left);
            postorder(root->right);
            traverse_path.push_back(root->val);
        }
    }

    std::vector<int> getPath()
    {
        return traverse_path;
    }

private:
    std::vector<int> traverse_path;
};


int main( void)
{
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right = new TreeNode(5);
    root->right->left = new TreeNode(6);

    // pre-order traversal
    Traversal traver_pre = Traversal();
    traver_pre.preorder(root);
    auto pre_path = traver_pre.getPath();
    std::cout << "Pre-order Traversal:" << std::endl;
    for ( std::vector<int>::iterator it = pre_path.begin(); it != pre_path.end(); ++it)
    {
        std::cout << *it << '\t';
    }
    std::cout << '\n';

    // in-order traversal
    Traversal traver_in = Traversal();
    traver_in.inorder(root);
    auto in_path = traver_in.getPath();
    std::cout << "In-order Traversal:" << std::endl;
    for ( std::vector<int>::iterator it = in_path.begin(); it != in_path.end(); ++it)
    {
        std::cout << *it << '\t';
    }
    std::cout << '\n';

    // post-order traversal
    Traversal traver_post = Traversal();
    traver_post.postorder(root);
    auto post_path = traver_post.getPath();
    std::cout << "Post-order Traversal:" << std::endl;
    for ( std::vector<int>::iterator it = post_path.begin(); it != post_path.end(); ++it)
    {
        std::cout << *it << '\t';
    }
    std::cout << '\n';

    // free memory for TreeNode:
    //delete root;
    freeTreeNode(root);     // recursively delete memory used by TreenNode

    return 0;
}
