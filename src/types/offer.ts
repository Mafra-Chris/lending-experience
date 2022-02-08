
export interface Offer {
  type: string;
  amountPerc: number;
  interest: number;
  taxValue: number;
  id: number;
  installments?: number
}
