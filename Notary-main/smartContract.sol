//SPDX-License-Identifier: GPL-3.0

pragma solidity 0.8.7;

// Creating a contract for the notary
contract notary {
    //This is the structure item which represents the Legal Documents sold between Legal Parties on notary
    struct Item {
        string document;    //name of the good
        string documentDetails;     //description of the product
        address payable seller;     //seller's crypto address
        uint id;            //Legal Document id which shall be displayed to the customers on the frontend
        uint itemPrice;     //price of the product
        address customer;   //address of the customer
        bool isVerified;   //boolean variable which decides whether the Document is verified or not
    }

    // list of the different Legal Docments sold between Legal Parties on notary
    Item[] public items; 

    // determines the id of the Transaction
    uint idNumber=1;        

    // Utility events required for the smooth functioning of our contract
    event registerationDone(string document, uint id, address seller );
    event bought( uint id, address customer);
    event itemVerified(uint id);

    // registers the item in the blockchain
    function registerItem( string memory _itemName, string memory _details, uint _price) public {
        require (_price>0, "Price should not be 0!" ); // checks if price>0
        Item memory object;
        object.document=_itemName;
        object.documentDetails=_details;
        object.seller=payable(msg.sender);
        object.id=idNumber++;
        object.itemPrice=_price* 10**18;
        items.push(object);
        emit registerationDone(_itemName, object.id, msg.sender);
    }

    // customer can buy the item 
    function buyItem( uint _itemID) payable public {
        // Amount should match the price
        require(items[_itemID-1].itemPrice==msg.value, "Please enter the correct amount!"); 
        //seller cant be buyer
        require(items[_itemID-1].seller!=msg.sender, "Customer and Seller should not be the same!"); 
        items[_itemID-1].customer=msg.sender;
        emit bought(_itemID, msg.sender);
    }

    // Notary can set isVerified true if the item is verified
    function isVerificationDone(uint _itemID) public {
        //seller cant confirm
        require (items[_itemID-1].customer==msg.sender, "The confirmation can be made only by the buyer");
        items[_itemID-1].isVerified = true;
        items[_itemID-1].seller.transfer(items[_itemID-1].itemPrice);
        emit itemVerified(_itemID);
    }

    // displays all the items 
    function getItems() public view returns (Item [] memory) {
        return items;
    }
}
