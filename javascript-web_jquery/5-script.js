// script that adds a <li> element to a list
const $ = window.$;

const $listElem = $('ul.my_list');
const $addItemElem = $('div#add_item');

$addItemElem.on('click', () => {
  $listElem.append('<li>Item</li>');
});
