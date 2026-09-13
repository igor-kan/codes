#[derive(Default)]
pub struct Trie { children: [Option<Box<Trie>>;26], end:bool }
impl Trie {
    pub fn insert(&mut self,w:&str){
        let mut n=self; for c in w.bytes(){ let i=(c-b'a')as usize;
            n=n.children[i].get_or_insert_with(Default::default); } n.end=true;
    }
    pub fn search(&self,w:&str)->bool{
        let mut n=self; for c in w.bytes(){ let i=(c-b'a')as usize;
            match &n.children[i]{ None=>return false, Some(x)=>n=x } } n.end
    }
}