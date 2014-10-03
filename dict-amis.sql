CREATE TABLE amis (
    title text,
    example text,
    en text,
    cmn text);
CREATE INDEX en_amis ON amis (en);
CREATE INDEX cmn_amis ON amis (cmn);
CREATE INDEX ex_amis ON amis (example);
